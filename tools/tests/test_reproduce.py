"""Validate lockfile gating in a disposable copy without installing packages."""

import contextlib
import importlib.util
import io
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]


class ReproduceLockTest(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="reproduce-tools-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        source = self.root / "tools/reproduce.py"
        source.parent.mkdir()
        shutil.copyfile(TOOLS / "reproduce.py", source)
        spec = importlib.util.spec_from_file_location("isolated_reproduce", source)
        self.tool = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.tool)
        self.tool.TARGET.mkdir(parents=True)
        self.lock = self.tool.TARGET / "requirements.lock.txt"

    def assert_rejected_before_environment_setup(self):
        with patch.object(self.tool.venv, "EnvBuilder") as environment, patch.object(self.tool.subprocess, "run") as run:
            with self.assertRaises(SystemExit) as stopped:
                self.tool.check()
            self.assertIsInstance(stopped.exception.code, str)
            self.assertIn("真实依赖锁文件", stopped.exception.code)
            environment.assert_not_called()
            run.assert_not_called()
        self.assertFalse(self.tool.REPORT.exists())
        self.assertFalse((self.tool.TARGET / ".venv").exists())

    def test_missing_empty_whitespace_and_comments_are_rejected(self):
        self.assert_rejected_before_environment_setup()
        for content in ("", " \n\t\n", "# 尚未冻结\n", "  # 说明\n\n\t# another comment\n"):
            with self.subTest(content=content):
                self.lock.write_text(content, encoding="utf-8")
                self.assert_rejected_before_environment_setup()

    def test_actual_default_template_is_rejected(self):
        template = TOOLS.parent / "handbook/templates/requirements.lock.txt"
        self.lock.write_text(template.read_text(encoding="utf-8"), encoding="utf-8")
        self.assert_rejected_before_environment_setup()

    def test_not_done_placeholder_remains_rejected(self):
        self.lock.write_text("example-package==1.2.3\n# NOT_DONE\n", encoding="utf-8")
        self.assert_rejected_before_environment_setup()

    def test_nonempty_requirements_keep_the_existing_pipeline(self):
        self.lock.write_text("# Frozen dependencies\nexample-package==1.2.3\n", encoding="utf-8")
        fake_result = subprocess.CompletedProcess(args=[], returncode=0, stdout="fixture output\n", stderr="")
        with patch.object(self.tool.venv, "EnvBuilder") as environment, patch.object(self.tool.subprocess, "run", return_value=fake_result) as run, contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaises(SystemExit) as stopped:
                self.tool.check()
            self.assertEqual(stopped.exception.code, 0)
            environment.assert_called_once_with(with_pip=True)
            environment.return_value.create.assert_called_once_with(self.tool.TARGET / ".venv")
            self.assertEqual(run.call_count, 2)
            self.assertEqual(run.call_args_list[0].args[0][1:5], ["-m", "pip", "install", "-r"])
            self.assertEqual(run.call_args_list[1].args[0][1:4], ["-m", "unittest", "discover"])
        self.assertTrue(self.tool.REPORT.is_file())


if __name__ == "__main__":
    unittest.main()
