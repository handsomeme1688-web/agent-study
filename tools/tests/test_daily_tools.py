"""Exercise the CLI in disposable workspaces, never in the student's project."""

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
PASSING = """import unittest
class Example(unittest.TestCase):
    def test_example(self):
        self.assertEqual(2 + 2, 4)
"""
FAILING = PASSING.replace("2 + 2, 4", "2 + 2, 5")


class DailyToolsTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="daily-tools-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.project = self.root / "repo-qa-agent"
        (self.root / "tools").mkdir()
        (self.root / "handbook/templates").mkdir(parents=True)
        for name in ("start_day.py", "check_day.py"):
            shutil.copyfile(TOOLS / name, self.root / "tools" / name)
        for package in ("tests", "algorithm_tests", "algorithms", "agent_lab"):
            self.write(f"{package}/__init__.py", "")
        self.manifest = {"days": {}, "files": {}}
        for number in (1, 2, 3, 7, 25, 27):
            tag = f"d{number:02d}"
            algorithm = f"algorithms/{tag}_example.py"
            algorithm_test = f"algorithm_tests/test_{tag}_example.py"
            new = [(algorithm, "算法练习"), (algorithm_test, "算法测试")]
            if number in (1, 2, 3, 25):
                business_test = "tests/test_d25_graph.py" if number == 25 else f"tests/test_{tag}_example.py"
                new.insert(0, (business_test, "业务测试"))
            if number == 25:
                new.insert(0, ("agent_lab/graph_agent.py", "选修图"))
            day = {
                "title": f"第{number}天", "new": new,
                "edit": [("agent_lab/retrieval.py", "实现检索与补读")],
                "out": [(f"reports/{tag}/demo.txt", "实际运行后产生")],
                "algorithm": {"code": algorithm, "test": algorithm_test},
            }
            if number == 27:
                day["edit"].append(("tests/test_d25_graph.py", "选修回归"))
            self.manifest["days"][str(number)] = day
            for path, description in new:
                template = self.root / "handbook/templates" / path
                template.parent.mkdir(parents=True, exist_ok=True)
                template.write_text(PASSING if "test_" in path else "# student skeleton\n", encoding="utf-8")
                self.manifest["files"][path] = {"template": str(template.relative_to(self.root))}
        self.save_manifest()
        self.write("agent_lab/retrieval.py", "# existing student work\n")

    def save_manifest(self):
        (self.root / "handbook/manifest.json").write_text(json.dumps(self.manifest), encoding="utf-8")

    def write(self, relative, text):
        target = self.project / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
        return target

    def run_tool(self, name, *args):
        return subprocess.run(
            [sys.executable, str(self.root / "tools" / name), *map(str, args)],
            cwd=self.root, text=True, capture_output=True,
        )

    def start(self, day):
        result = self.run_tool("start_day.py", day)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return result

    def test_start_is_repeatable_preserves_work_and_explains_next_step(self):
        self.start(3)
        target = self.write("algorithms/d03_example.py", "# my solution\n")
        result = self.start(3)
        self.assertEqual(target.read_text(), "# my solution\n")
        self.assertEqual((self.project / "agent_lab/retrieval.py").read_text(), "# existing student work\n")
        self.assertIn("KEEP", result.stdout)
        self.assertIn("实现检索与补读", result.stdout)
        self.assertIn("handbook/顺序版/day03.md", result.stdout)
        self.assertIn("--project-only", result.stdout)
        self.assertIn("--algorithm-only", result.stdout)
        self.assertFalse((self.project / "reports/d03/demo.txt").exists())

    def test_start_uses_optional_sequential_metadata(self):
        metadata = {"days": {"3": {"first_file": "repo-qa-agent/agent_lab/retrieval.py", "first_task": "先实现 search_docs 的参数校验"}}}
        (self.root / "handbook/sequential.json").write_text(json.dumps(metadata), encoding="utf-8")
        result = self.start(3)
        self.assertIn("先实现 search_docs 的参数校验", result.stdout)
        self.assertNotIn("repo-qa-agent/repo-qa-agent", result.stdout)

    def test_project_does_not_run_or_report_unfinished_algorithm(self):
        self.start(1)
        self.write("algorithm_tests/test_d01_example.py", FAILING)
        result = self.run_tool("check_day.py", 1, "--project-only")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertFalse((self.project / "reports/d01/algorithm.txt").exists())
        result = self.run_tool("check_day.py", 1, "--algorithm-only")
        self.assertEqual(result.returncode, 1)
        self.assertIn("FAILED (failures=1)", result.stdout)
        self.assertIn("EXIT_CODE=1", (self.project / "reports/d01/algorithm.txt").read_text())

    def test_algorithm_is_independent_of_failing_business_and_only_current_is_accepted(self):
        self.start(1)
        self.write("tests/test_d01_example.py", FAILING)
        result = self.run_tool("check_day.py", 1, "--algorithm-only", "--only-current")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertFalse((self.project / "reports/d01/unittest.txt").exists())
        result = self.run_tool("check_day.py", 1, "--project-only")
        self.assertEqual(result.returncode, 1)

    def test_default_runs_both_and_returns_failure(self):
        self.start(1)
        self.write("tests/test_d01_example.py", FAILING)
        result = self.run_tool("check_day.py", 1)
        self.assertEqual(result.returncode, 1)
        self.assertTrue((self.project / "reports/d01/unittest.txt").is_file())
        self.assertIn("EXIT_CODE=0", (self.project / "reports/d01/algorithm.txt").read_text())

    def test_missing_required_current_test_is_a_clear_failure(self):
        self.start(1)
        result = self.run_tool("check_day.py", 3, "--project-only", "--only-current")
        self.assertEqual(result.returncode, 1)
        self.assertIn("缺少计划要求", result.stdout)
        self.assertIn("tests/test_d03_example.py", result.stdout)
        self.assertNotIn("Ran 1 test", result.stdout)

    def test_registered_base_tests_are_required_only_when_their_day_is_due(self):
        self.manifest["base_tests"] = ["tests/test_d01_io.py", "tests/test_d03_retrieval.py", "tests/test_d04_config.py"]
        self.save_manifest()
        self.start(1)
        result = self.run_tool("check_day.py", 1, "--project-only")
        self.assertEqual(result.returncode, 1)
        self.assertIn("tests/test_d01_io.py", result.stdout)
        self.assertIn("基础固定测试须从项目原始版本恢复", result.stdout)
        self.write("tests/test_d01_io.py", PASSING)
        result = self.run_tool("check_day.py", 1, "--project-only")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.start(3)
        result = self.run_tool("check_day.py", 3, "--project-only", "--only-current")
        self.assertEqual(result.returncode, 1)
        self.assertIn("tests/test_d03_retrieval.py", result.stdout)
        self.write("tests/test_d03_retrieval.py", PASSING)
        result = self.run_tool("check_day.py", 3, "--project-only", "--only-current")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Ran 2 tests", result.stdout)

    def test_missing_algorithm_is_a_clear_failure(self):
        result = self.run_tool("check_day.py", 3, "--algorithm-only")
        self.assertEqual(result.returncode, 1)
        self.assertIn("缺少算法测试文件", result.stdout)

    def test_current_day_without_tests_falls_back_to_cumulative_tests(self):
        for day in (1, 2, 3):
            self.start(day)
        result = self.run_tool("check_day.py", 7, "--project-only", "--only-current")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("累计业务测试", result.stdout)
        self.assertIn("Ran 3 tests", result.stdout)
        result = self.run_tool("check_day.py", 3, "--project-only", "--only-current")
        self.assertEqual(result.returncode, 0)
        self.assertIn("Ran 1 test", result.stdout)

    def test_zero_tests_and_all_skipped_tests_fail(self):
        self.start(1)
        self.write("tests/test_d01_example.py", "# no assertions\n")
        result = self.run_tool("check_day.py", 1, "--project-only")
        self.assertEqual(result.returncode, 1)
        self.assertIn("没有运行任何测试", result.stdout)
        self.write("tests/test_d01_example.py", PASSING.replace("    def test_example", '    @unittest.skip("unfinished")\n    def test_example'))
        result = self.run_tool("check_day.py", 1, "--project-only")
        self.assertEqual(result.returncode, 1)
        self.assertIn("全部测试被跳过", result.stdout)

    def test_no_available_or_required_tests_does_not_pass(self):
        self.manifest["days"]["1"]["new"] = [entry for entry in self.manifest["days"]["1"]["new"] if not entry[0].startswith("tests/")]
        self.save_manifest()
        result = self.run_tool("check_day.py", 1, "--project-only")
        self.assertEqual(result.returncode, 1)
        self.assertIn("没有可运行的业务测试", result.stdout)

    def test_skip_optional_and_subsequent_cumulative_checks(self):
        for day in (1, 2, 3):
            self.start(day)
        result = self.run_tool("start_day.py", 25, "--skip-optional")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertFalse((self.project / "agent_lab/graph_agent.py").exists())
        self.assertFalse((self.project / "tests/test_d25_graph.py").exists())
        for day in (25, 27):
            result = self.run_tool("check_day.py", day, "--project-only", "--only-current")
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("跳过LangGraph", result.stdout)
            self.assertIn("Ran 3 tests", result.stdout)
        self.write("agent_lab/graph_agent.py", "# selected optional work\n")
        result = self.run_tool("check_day.py", 25, "--project-only", "--only-current")
        self.assertEqual(result.returncode, 1)
        self.assertIn("tests/test_d25_graph.py", result.stdout)

    def test_scope_flags_are_mutually_exclusive(self):
        result = self.run_tool("check_day.py", 1, "--project-only", "--algorithm-only")
        self.assertEqual(result.returncode, 2)
        self.assertFalse((self.project / "reports").exists())


if __name__ == "__main__":
    unittest.main()
