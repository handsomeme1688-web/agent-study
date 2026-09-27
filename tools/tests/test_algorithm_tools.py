"""Algorithm tooling checks use disposable fixtures, never student answers."""

import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import types
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
LOADER = importlib.util.spec_from_file_location("algorithm_tool_support", TOOLS / "algorithm_support.py")
SUPPORT = importlib.util.module_from_spec(LOADER)
LOADER.loader.exec_module(SUPPORT)
PASSING = "import unittest\nclass Example(unittest.TestCase):\n    def test_ok(self):\n        self.assertEqual(1, 1)\n"


class AlgorithmToolsTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="algorithm-tools-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.project = self.root / "repo-qa-agent"
        (self.root / "tools").mkdir()
        (self.root / "handbook").mkdir()
        for name in ("algorithm_support.py", "start_algorithms.py", "check_algorithms.py", "start_day.py", "check_day.py"):
            shutil.copyfile(TOOLS / name, self.root / "tools" / name)
        # Deliberately trivial fixture problems test orchestration, not answers.
        self.catalog = {"version": 1, "days": {str(day): {"topic": "工具夹具", "problem_ids": [1, 49, 169]} for day in range(1, 31)}, "problems": {}}
        for number in (1, 49, 169):
            self.catalog["problems"][str(number)] = {"id": number, "title": "夹具", "slug": f"fixture-{number}", "kind": "function", "method": "echo", "params": "values: list[int]", "returns": "list[int]", "cases": [{"args": [values], "expected": values} for values in ([], [1], [1, 2])]}
        self.save_catalog()

    def save_catalog(self):
        (self.root / "handbook/algorithms_110.json").write_text(json.dumps(self.catalog), encoding="utf-8")

    def write(self, relative, text):
        path = self.project / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def run_tool(self, name, *args):
        return subprocess.run([sys.executable, str(self.root / "tools" / name), *map(str, args)], cwd=self.root, capture_output=True, text=True)

    def start(self, day="A01"):
        result = self.run_tool("start_algorithms.py", day)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return result

    def solve_fixtures(self):
        self.start()
        for spec in self.catalog["problems"].values():
            code, _ = SUPPORT.problem_paths(spec)
            self.write(code, "class Solution:\n    def echo(self, values):\n        return values\n")

    def test_scaffold_preserves_work_and_initial_todos_fail(self):
        result = self.start()
        self.assertIn("--problem 1", result.stdout)
        self.assertIn("3 题", result.stdout)
        note = self.project / "notes/algorithms/a01.md"
        self.assertIn("独立或提示后完成", note.read_text())
        note.write_text("# my own review\n")
        result = self.run_tool("check_algorithms.py", "A01")
        self.assertEqual(result.returncode, 1)
        self.assertIn("NotImplementedError", result.stdout)
        code, _ = SUPPORT.problem_paths(self.catalog["problems"]["1"])
        target = self.write(code, "# student's own work\n")
        support = self.write("algorithm_tests/interview/_support.py", "# student's helper notes\n")
        result = self.start()
        self.assertEqual(target.read_text(), "# student's own work\n")
        self.assertEqual(support.read_text(), "# student's helper notes\n")
        self.assertEqual(note.read_text(), "# my own review\n")
        self.assertIn("KEEP", result.stdout)

    def test_day_and_single_problem_checks_have_separate_aggregates(self):
        self.solve_fixtures()
        result = self.run_tool("check_algorithms.py", "1")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        aggregate = self.project / "reports/algorithms/a01/summary.txt"
        original = aggregate.read_text()
        self.assertIn("3/3 题", original)
        result = self.run_tool("check_algorithms.py", "A01", "--problem", 1)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("1/1 题", result.stdout)
        self.assertEqual(aggregate.read_text(), original)
        self.assertTrue((aggregate.parent / "summary_lc0001.txt").exists())

    def test_missing_empty_and_all_skipped_are_individual_failures(self):
        self.solve_fixtures()
        _, path = SUPPORT.problem_paths(self.catalog["problems"]["1"])
        target = self.project / path
        target.unlink()
        result = self.run_tool("check_algorithms.py", "A01")
        self.assertEqual(result.returncode, 1)
        self.assertIn("缺少算法测试文件", result.stdout)
        self.assertIn("2/3 题", result.stdout)
        self.write(path, "# accidentally empty\n")
        result = self.run_tool("check_algorithms.py", "A01")
        self.assertEqual(result.returncode, 1)
        self.assertIn("没有运行任何测试", result.stdout)
        self.write(path, PASSING.replace("    def test_ok", '    @unittest.skip("unfinished")\n    def test_ok'))
        result = self.run_tool("check_algorithms.py", "A01")
        self.assertEqual(result.returncode, 1)
        self.assertIn("全部测试被跳过", result.stdout)
        self.assertIn("2/3 题", result.stdout)

    def test_invalid_day_and_foreign_problem_fail_before_reports(self):
        for args in (("A31",), ("A01", "--problem", "999")):
            result = self.run_tool("check_algorithms.py", *args)
            self.assertEqual(result.returncode, 2)
        self.assertFalse((self.project / "reports").exists())

    def test_symlink_cannot_write_outside_practice_root(self):
        outside = self.root / "outside"
        outside.mkdir()
        self.project.mkdir()
        (self.project / "algorithms").symlink_to(outside, target_is_directory=True)
        result = self.run_tool("start_algorithms.py", "A01")
        self.assertEqual(result.returncode, 2)
        self.assertIn("非法输出路径", result.stderr)
        self.assertEqual(list(outside.iterdir()), [])

    def test_day_three_routes_to_a01_and_keeps_legacy_file(self):
        manifest = {"days": {"3": {"title": "夹具", "new": [["algorithms/old.py", "旧算法"], ["algorithm_tests/test_old.py", "旧测试"]], "edit": [["agent_lab/example.py", "实现业务"]], "out": [], "algorithm": {"code": "algorithms/old.py", "test": "algorithm_tests/test_old.py"}}}, "files": {}}
        (self.root / "handbook/manifest.json").write_text(json.dumps(manifest))
        self.write("algorithms/old.py", "# previous progress\n")
        self.write("agent_lab/example.py", "# current work\n")
        result = self.run_tool("start_day.py", 3)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("A01", result.stdout)
        self.assertEqual((self.project / "algorithms/old.py").read_text(), "# previous progress\n")
        self.assertFalse((self.project / "algorithm_tests/test_old.py").exists())
        self.solve_fixtures()
        result = self.run_tool("check_day.py", 3, "--algorithm-only")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        report = self.project / "reports/d03/algorithm.txt"
        self.assertIn("3/3 题", report.read_text())
        self.assertFalse((self.project / "reports/d03/unittest.txt").exists())

    def test_a30_is_independently_available(self):
        result = self.start("A30")
        self.assertIn("A30", result.stdout)
        self.assertFalse((self.project / "agent_lab").exists())


class GeneratedRunnerTest(unittest.TestCase):
    def setUp(self):
        self.namespace = {}
        exec(SUPPORT.STRUCTURES, self.namespace)
        exec(SUPPORT.TEST_SUPPORT.replace("from algorithms.interview._structures import ListNode, TreeNode, Node", ""), self.namespace)

    def run_case(self, callback, case, kind="function", returns=None):
        module = types.SimpleNamespace(Solution=lambda: types.SimpleNamespace(exercise=callback))
        self.namespace["run_case"](self, module, {"kind": kind, "method": "exercise", "returns": returns}, case)

    def test_standard_decoding_and_comparators(self):
        self.run_case(lambda head: head.next, {"args": [{"$list": [1, 2]}], "expected": [2]})
        self.run_case(lambda root: root.right, {"args": [{"$tree": [1, None, 2, 3]}], "expected": [2, 3]})
        self.run_case(lambda: [[2, 1], [3]], {"args": [], "expected": [[3], [1, 2]], "comparator": "unordered_nested"})
        self.run_case(lambda: [[2, 1], [3]], {"args": [], "expected": [[3], [2, 1]], "comparator": "unordered"})
        with self.assertRaises(AssertionError):
            self.run_case(lambda: [[2, 1]], {"args": [], "expected": [[1, 2]], "comparator": "unordered"})
        self.run_case(lambda: 2, {"args": [], "expected": [1, 2], "comparator": "any_of"})
        self.run_case(lambda: 0.1 + 0.2, {"args": [], "expected": 0.3, "comparator": "approx"})
        self.run_case(lambda values: values.reverse(), {"args": [[1, 2]], "expected": [2, 1], "in_place_arg": 0})

    def test_cycle_and_intersection_require_node_identity(self):
        self.run_case(lambda head: head.next, {"args": [[1, 2], 1], "expected_index": 1}, "cycle_node")
        self.run_case(lambda head: head.next.next is head, {"args": [[1, 2], 0], "expected": True}, "cycle_bool")
        self.run_case(lambda head: False, {"args": [[], -1], "expected": False}, "cycle_bool")
        node_type = self.namespace["ListNode"]
        with self.assertRaises(AssertionError):
            self.run_case(lambda head: node_type(head.next.val), {"args": [[1, 2], 1], "expected_index": 1}, "cycle_node")
        self.run_case(lambda a, b: a.next, {"a_prefix": [1], "b_prefix": [2], "shared": [3, 4]}, "intersection")

    def test_lca_bst_and_flatten_validate_structure(self):
        self.run_case(lambda root, p, q: root, {"args": [[2, 1, 3], 1, 3], "expected": 2}, "lca")
        tree = self.namespace["tree"]
        self.run_case(lambda values: tree([2, 1, 3]), {"args": [[1, 2, 3]], "expected": [1, 2, 3]}, "balanced_bst")
        with self.assertRaises(AssertionError):
            self.run_case(lambda values: tree([1, None, 2, None, 3]), {"args": [[1, 2, 3]], "expected": [1, 2, 3]}, "balanced_bst")
        def flatten(root):
            right = root.right
            root.right, root.left = root.left, None
            root.right.right = right
        self.run_case(flatten, {"args": [[1, 2, 3]], "expected": [1, 2, 3]}, "flatten")
        with self.assertRaises(AssertionError):
            self.run_case(lambda root: None, {"args": [[1, 2, 3]], "expected": [1, 2, 3]}, "flatten")

    def test_random_list_rejects_shallow_copy(self):
        node_type = self.namespace["Node"]
        def copy_one(head):
            node = node_type(head.val)
            node.random = node
            return node
        case = {"args": [[[7, 0]]], "expected": [[7, 0]]}
        self.run_case(copy_one, case, "random_list")
        with self.assertRaises(AssertionError):
            self.run_case(lambda head: head, case, "random_list")

    def test_design_sequence_and_empty_structures(self):
        class Box:
            def __init__(self, value):
                self.value = value
            def read(self):
                return self.value
        self.namespace["run_case"](self, types.SimpleNamespace(Box=Box), {"kind": "design", "class_name": "Box"}, {"operations": ["Box", "read"], "arguments": [[2], []], "expected": [None, 2]})
        self.run_case(lambda root: root, {"args": [{"$tree": []}], "expected": []}, returns="Optional[TreeNode]")
        self.run_case(lambda head: head, {"args": [{"$list": []}], "expected": []}, returns="Optional[ListNode]")
        with self.assertRaises(AssertionError):
            self.run_case(lambda root: None, {"args": [{"$tree": []}], "expected": []}, returns="list[int]")
        with self.assertRaises(AssertionError):
            self.run_case(lambda nums: None, {"args": [[]], "expected": []}, returns="list[list[int]]")
        self.run_case(lambda root: None, {"args": [[]], "expected": []}, "flatten")
        self.run_case(lambda values: None, {"args": [[]], "expected": []}, "balanced_bst")


if __name__ == "__main__":
    unittest.main()
