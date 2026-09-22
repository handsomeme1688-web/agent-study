import json
import unittest
from unittest.mock import patch
from agent_lab.tools import parse_decision, dispatch

class TestD05(unittest.TestCase):
    def parse(self,obj): return parse_decision(json.dumps(obj,ensure_ascii=False))
    def test_valid_search_and_default(self):
        out=self.parse({'type':'tool','name':'search_docs','arguments':{'query':'工具'}})
        self.assertEqual(out['arguments']['k'],3)
    def test_valid_read(self):
        self.assertEqual(self.parse({'type':'tool','name':'read_chunk','arguments':{'chunk_id':'a'}})['name'],'read_chunk')
    def test_final_default(self):
        self.assertEqual(self.parse({'type':'final','answer':'证据不足'})['citations'],[])
    def test_malformed_json(self):
        with self.assertRaises(ValueError): parse_decision('{not json')
    def test_reject_invalid(self):
        bad=[[],{'type':'other'},
             {'type':'tool','name':'delete_file','arguments':{}},
             {'type':'tool','name':'search_docs','arguments':{'query':''}},
             {'type':'tool','name':'search_docs','arguments':{'query':123}},
             {'type':'tool','name':'search_docs','arguments':{'query':'x','k':True}},
             {'type':'tool','name':'search_docs','arguments':{'query':'x','k':9}},
             {'type':'tool','name':'read_chunk','arguments':{'path':'/etc/passwd'}},
             {'type':'tool','name':'read_chunk','arguments':{'chunk_id':'a','path':'/etc/passwd'}},
             {'type':'final','answer':'','citations':[]},
             {'type':'final','answer':'x','citations':[3]},
             {'type':'final','answer':'x','debug':'extra'}]
        for obj in bad:
            with self.subTest(obj=obj),self.assertRaises(ValueError): self.parse(obj)
    def test_dispatch_good(self):
        with patch('agent_lab.tools.search_docs',return_value=[{'id':'a'}]) as fn:
            self.assertEqual(dispatch([],'search_docs',{'query':'q'}),[{'id':'a'}])
            fn.assert_called_once_with([],'q',3)
    def test_dispatch_blocks_before_execution(self):
        with patch('agent_lab.tools.search_docs') as fn:
            with self.assertRaises(ValueError): dispatch([],'search_docs',{'query':3})
            fn.assert_not_called()
