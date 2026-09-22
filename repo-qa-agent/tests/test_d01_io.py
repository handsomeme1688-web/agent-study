import json
import tempfile
import unittest
from pathlib import Path
from agent_lab.io import read_text, write_jsonl

class TestD01(unittest.TestCase):
    def test_utf8(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'a.md';p.write_text('你好，Agent。\n',encoding='utf-8')
            self.assertEqual(read_text(str(p)), '你好，Agent。\n')
    def test_empty(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'empty';p.write_text('',encoding='utf-8')
            self.assertEqual(read_text(str(p)), '')
    def test_missing(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(FileNotFoundError): read_text(str(Path(tmp)/'missing'))
    def test_jsonl_roundtrip_and_chinese(self):
        rows=[{'id':1,'text':'工具\n下一行'},{'id':2,'text':'检索'}]
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'nested'/'out.jsonl';write_jsonl(rows,str(p))
            raw=p.read_text(encoding='utf-8');lines=raw.splitlines()
            self.assertEqual(len(lines),2);self.assertIn('工具',raw)
            self.assertEqual([json.loads(x) for x in lines],rows)
    def test_overwrite_not_append(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'out.jsonl';write_jsonl([{'id':1}],str(p));write_jsonl([{'id':2}],str(p))
            self.assertEqual([json.loads(x) for x in p.read_text().splitlines()],[{'id':2}])
    def test_empty_records(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'out.jsonl';write_jsonl([],str(p));self.assertEqual(p.read_text(),'')
