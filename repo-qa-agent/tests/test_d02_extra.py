"""D02 待编写测试：自己补连续标题用例。契约见当天任务卡。"""
import unittest

from agent_lab.chunking import split_markdown

class TestD02Student(unittest.TestCase):
    def test_required_cases(self):
        # 连续标题：两行紧挨着，中间没有正文
        rows = split_markdown('# A\n## B', 'a')
        self.assertEqual(len(rows), 2)
        self.assertEqual([(r['start_line'], r['end_line']) for r in rows], [(1, 1), (2, 2)])
        self.assertEqual(rows[1]['text'], '## B')

        rows2 = split_markdown('# 只有一个标题', 'a')
        self.assertEqual(len(rows2), 1)
        self.assertEqual([(r['start_line'], r['end_line']) for r in rows2], [(1, 1)])
        self.assertEqual(rows2[0]['text'], '# 只有一个标题')
        self.assertEqual(rows2[0]['title'], '只有一个标题')

        rows3 = split_markdown('#### 四级标题\n内容', 'a')
        self.assertEqual(len(rows3), 1)
        self.assertEqual([(r['start_line'], r['end_line']) for r in rows3], [(1, 2)])
        self.assertEqual(rows3[0]['text'], '#### 四级标题\n内容')
        self.assertEqual(rows3[0]['title'], '四级标题')

if __name__ == "__main__":
    unittest.main()
