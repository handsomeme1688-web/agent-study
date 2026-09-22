def evaluate_rows(rows: list[dict], query_fn, config: dict) -> list[dict]:
    """D14：保留每题原始输出，失败也占一条记录。"""
    raise NotImplementedError("请按当天任务卡完成 evaluate_rows")

def summarize_scores(scores: list[dict]) -> dict:
    """D14：按统一口径汇总人工评分，不发模型请求。"""
    raise NotImplementedError("请按当天任务卡完成 summarize_scores")

