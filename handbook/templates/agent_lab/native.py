def build_tool_schema() -> list[dict]:
    """D08：只注册课程允许的工具。"""
    raise NotImplementedError("请按当天任务卡完成 build_tool_schema")

def normalize_tool_call(call: dict) -> dict:
    """D08：解析name/arguments并校验。"""
    raise NotImplementedError("请按当天任务卡完成 normalize_tool_call")

def build_tool_message(call_id: str, result) -> dict:
    """D08：构造匹配调用ID的原生工具结果消息。"""
    raise NotImplementedError("请按当天任务卡完成 build_tool_message")

