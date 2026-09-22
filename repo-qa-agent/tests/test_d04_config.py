import unittest
from agent_lab.config import get_config

class TestD04(unittest.TestCase):
    def setUp(self):
        self.env={'LLM_API_KEY':' secret-demo-not-real ','LLM_BASE_URL':' https://example.invalid/v1 ',
                  'LLM_MODEL_ID':' demo-model '}
    def test_normalize(self):
        self.assertEqual(get_config(self.env),{'api_key':'secret-demo-not-real','base_url':'https://example.invalid/v1','model':'demo-model'})
    def test_missing_or_empty(self):
        for key in self.env:
            for value in [None,'   ']:
                env=dict(self.env)
                if value is None: del env[key]
                else: env[key]=value
                with self.subTest(key=key,value=value),self.assertRaises(ValueError): get_config(env)
    def test_bad_url_no_secret(self):
        self.env['LLM_BASE_URL']='file:///tmp/abc'
        with self.assertRaises(ValueError) as ctx: get_config(self.env)
        self.assertNotIn('secret-demo-not-real',str(ctx.exception))
