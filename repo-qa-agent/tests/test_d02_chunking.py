import unittest
from pathlib import Path
from agent_lab.chunking import split_markdown

class TestD02(unittest.TestCase):
    def test_fixture_exact(self):
        text=(Path(__file__).resolve().parents[1]/'fixtures'/'mini.md').read_text(encoding='utf-8')
        rows=split_markdown(text,'mini.md')
        self.assertEqual(len(rows),3)
        self.assertEqual([r['title'] for r in rows],['工具','检索','安全'])
        self.assertEqual([(r['start_line'],r['end_line']) for r in rows],[(1,3),(4,6),(7,8)])
        for r in rows:
            self.assertEqual(r['id'],f"mini.md#L{r['start_line']}-L{r['end_line']}")
            self.assertEqual(r['source'],'mini.md')
            self.assertEqual(r['text'],'\n'.join(text.splitlines()[r['start_line']-1:r['end_line']]))
    def test_empty(self): self.assertEqual(split_markdown('', 'a'),[])
    def test_whitespace(self): self.assertEqual(split_markdown(' \n\n','a'),[])
    def test_no_heading(self):
        rows=split_markdown('正文\n第二行','a');self.assertEqual(len(rows),1)
        self.assertEqual(rows[0]['title'],'未分节');self.assertEqual(rows[0]['end_line'],2)
    def test_preface(self):
        rows=split_markdown('前言\n# 标题\n内容','a')
        self.assertEqual([r['title'] for r in rows],['未分节','标题'])
        self.assertEqual(rows[1]['start_line'],2)
    def test_final_flush_and_duplicate_heading(self):
        rows=split_markdown('# A\nx\n# A\ny','a')
        self.assertEqual(len(rows),2);self.assertNotEqual(rows[0]['id'],rows[1]['id'])
        self.assertEqual(rows[1]['text'],'# A\ny')
