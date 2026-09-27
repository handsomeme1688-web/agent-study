"""Verify HWD scaffolding in disposable folders without services or network."""

import ast
import contextlib
import importlib.util
import io
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]


class HwdScaffoldTest(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="hwd-scaffold-test-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.script = self.root / "start_hwd.py"
        shutil.copyfile(TOOLS / "start_hwd.py", self.script)
        self.project = self.root / "practice"

    def start(self, day, root=None):
        return subprocess.run(
            [sys.executable, str(self.script), str(day), "--root", str(root or self.project)],
            cwd=self.root, text=True, capture_output=True,
        )

    def test_all_ten_days_generate_valid_python_and_discover_42_tests(self):
        for day in range(1, 11):
            with self.subTest(day=day):
                result = self.start(day)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertIn(f"tests.test_day{day:02d}", result.stdout)
                self.assertIn("现在编写", result.stdout)
        files = list(self.project.rglob("*.py"))
        self.assertEqual(len(files), 23)
        for path in files:
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        discover = subprocess.run(
            [
                sys.executable, "-c",
                "import unittest\n"
                "loader = unittest.TestLoader()\n"
                "suite = loader.discover('tests')\n"
                "assert not loader.errors, loader.errors\n"
                "print(suite.countTestCases())\n",
            ],
            cwd=self.project, text=True, capture_output=True,
        )
        self.assertEqual(discover.returncode, 0, discover.stdout + discover.stderr)
        self.assertEqual(discover.stdout.strip(), "42")

    def test_repeat_generation_preserves_student_work(self):
        result = self.start(1)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        target = self.project / "src/contracts.py"
        target.write_text("# student's completed implementation\n", encoding="utf-8")
        test_path = self.project / "tests/test_day01.py"
        original_test = test_path.read_bytes()
        result = self.start(1)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(target.read_text(), "# student's completed implementation\n")
        self.assertEqual(test_path.read_bytes(), original_test)
        self.assertIn("保留已有文件", result.stdout)

    def test_original_hwd_paths_are_rejected_before_any_write(self):
        spec = importlib.util.spec_from_file_location("isolated_start_hwd", self.script)
        tool = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(tool)
        for target in (
            "/home/handsomeme/PythonProjects/hwd",
            "/home/handsomeme/PythonProjects/hwd/hwd-new",
        ):
            with self.subTest(target=target):
                stderr = io.StringIO()
                with (
                    patch.object(sys, "argv", [str(self.script), "1", "--root", target]),
                    patch.object(Path, "mkdir", side_effect=AssertionError("unexpected directory write")) as mkdir,
                    patch.object(Path, "open", side_effect=AssertionError("unexpected file open")) as open_file,
                    contextlib.redirect_stderr(stderr),
                ):
                    with self.assertRaises(SystemExit) as stopped:
                        tool.main()
                    self.assertEqual(stopped.exception.code, 2)
                    mkdir.assert_not_called()
                    open_file.assert_not_called()
                self.assertIn("不能写入原 hwd", stderr.getvalue())

    def test_symlink_cannot_escape_the_practice_directory(self):
        self.project.mkdir()
        outside = self.root / "outside"
        outside.mkdir()
        (self.project / "src").symlink_to(outside, target_is_directory=True)
        result = self.start(1)
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertIn("符号链接", result.stderr)
        self.assertEqual(list(outside.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
