"""D01 待编写测试：自己写中文路径的边界测试。契约见当天任务卡。"""
import json
from pathlib import Path
import tempfile
import unittest
from agent_lab.io import read_text, write_jsonl
class TestD01Student(unittest.TestCase):
    def test_required_cases(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            folder = Path(tmpdir)/"中文目录"
            folder.mkdir()
            target = folder/"中文文件.jsonl"
            records = [{"name":"张三","age":20},{"name":"李四","age":30}]
            write_jsonl(records, target)

            read_records = [json.loads(line) for line in read_text(target).splitlines()]                                                                                                                                                                                                                                                                                                     
                                                                                                                                                                                                 
            self.assertEqual(records, read_records)
        # self.fail("TODO_STUDENT_TEST: 请按日卡写真实断言，不要删除此项后冒充测试完成")

if __name__ == "__main__":
    unittest.main()
