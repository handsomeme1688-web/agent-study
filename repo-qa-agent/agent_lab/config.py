from collections.abc import Mapping

def get_config(env: Mapping[str, str]) -> dict:
    """D4：必填 LLM_API_KEY/LLM_BASE_URL/LLM_MODEL_ID，先 strip。
    缺少或空白抛 ValueError，只报告字段名，禁止把密钥值放进报错。
    返回 {'api_key': ..., 'base_url': ..., 'model': ...}。
    base_url 必须以 http:// 或 https:// 开头。
    此函数不发网络请求，也不会自动读取 .env。
    """
    raise NotImplementedError("D4: 实现 get_config")
