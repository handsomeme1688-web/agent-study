"""D04 学生测试：配置校验出错时不得泄露密钥值。契约见当天任务卡。"""
import unittest

from agent_lab.config import get_config


class TestD04Student(unittest.TestCase):
    def test_blank_model_does_not_leak_key(self):
        fake_key = "sk-canary-9f3a2b7c-do-not-leak"
        env = {
            "LLM_API_KEY": fake_key,
            "LLM_BASE_URL": "https://example.invalid/v1",
            "LLM_MODEL_ID": "   ",                     # 空白 → 触发 ValueError
        }

        with self.assertRaises(ValueError) as ctx:
            get_config(env)

        message = str(ctx.exception)
        self.assertIn("LLM_MODEL_ID", message)         # 确实因模型名为空而报错
        self.assertNotIn(fake_key, message)            # 密钥没有出现在报错里


if __name__ == "__main__":
    unittest.main()