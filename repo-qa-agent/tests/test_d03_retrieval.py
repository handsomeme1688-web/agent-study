import copy
import unittest
from agent_lab.retrieval import search_docs, read_chunk

class TestD03(unittest.TestCase):
    def setUp(self):
        self.rows=[{'id':'b','text':'agent tool'},{'id':'a','text':'AGENT tool read'},
                   {'id':'c','text':'只读 检索 片段'}]
    def test_order(self):
        self.assertEqual([r['id'] for r in search_docs(self.rows,'agent tool',2)],['a','b'])
    def test_unique_words(self):
        self.assertEqual(search_docs(self.rows,'agent agent',1)[0]['score'],1)
    def test_empty_and_no_hit(self):
        self.assertEqual(search_docs(self.rows,'  '),[])
        self.assertEqual(search_docs(self.rows,'不存在的词'),[])
    def test_chinese(self): self.assertEqual(search_docs(self.rows,'检索 片段')[0]['id'],'c')
    def test_invalid_k(self):
        for k in [0,-1,6,True,1.5,'3']:
            with self.subTest(k=k), self.assertRaises(ValueError): search_docs(self.rows,'agent',k)
    def test_does_not_mutate(self):
        old=copy.deepcopy(self.rows);result=search_docs(self.rows,'agent')
        self.assertEqual(old,self.rows);result[0]['text']='changed';self.assertEqual(old,self.rows)
    def test_read(self): self.assertEqual(read_chunk(self.rows,'a')['text'],'AGENT tool read')
    def test_unknown_id(self):
        with self.assertRaises(KeyError): read_chunk(self.rows,'../../secret')
