def build_context(system: str, question: str, history: list[dict], evidence: list[dict], max_chars: int = 6000) -> list[dict]:
    """D16：保留system/问题，先删最旧历史；本课程是字符上限。"""
    raise NotImplementedError("请按当天任务卡完成 build_context")

