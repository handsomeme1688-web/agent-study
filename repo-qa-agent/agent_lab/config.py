from collections.abc import Mapping
import os


def get_config(env: Mapping[str, str]) -> dict:
    """D4：必填 LLM_API_KEY/LLM_BASE_URL/LLM_MODEL_ID，先 strip。
    缺少或空白抛 ValueError，只报告字段名，禁止把密钥值放进报错。
    返回 {'api_key': ..., 'base_url': ..., 'model': ...}。
    base_url 必须以 http:// 或 https:// 开头。
    此函数不发网络请求，也不会自动读取 .env。
    """
    pairs = (
        ("LLM_API_KEY", "api_key"),
        ("LLM_BASE_URL", "base_url"),
        ("LLM_MODEL_ID", "model"),
    )

    config = {}
    for var_name, key in pairs:
        raw = env.get(var_name)
        value = raw.strip() if isinstance(raw, str) else ""
        if not value:
            raise ValueError(f"缺少或空白：{var_name}")
        config[key] = value

    if not config["base_url"].startswith(("http://", "https://")):
        raise ValueError("LLM_BASE_URL 必须以 http:// 或 https:// 开头")

    return config

    
