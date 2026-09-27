"""D03 待编写测试：自己补同分排序和原数据不被修改用例。契约见当天任务卡。"""
import unittest

from agent_lab.retrieval import search_docs

class TestD03Student(unittest.TestCase):
    def test_required_cases(self):
        rows=[{"id":"b","text":"agent tool"},{"id":"a","text":"AGENT tool read"}]
        self.assertEqual(search_docs(rows,"agent",3),
                         [{"id":"a","text":"AGENT tool read","score":1},
                          {"id":"b","text":"agent tool","score":1}])
        self.assertEqual(rows,[{"id":"b","text":"agent tool"},{"id":"a","text":"AGENT tool read"}])

if __name__ == "__main__":
    unittest.main()
