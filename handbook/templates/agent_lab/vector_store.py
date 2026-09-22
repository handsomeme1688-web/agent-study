class LocalVectorStore:
    def __init__(self, path: str, collection: str, dim: int) -> None:
        """按对应日卡填写；当前未实现。"""
        raise NotImplementedError("请按当天任务卡完成 __init__")

    def upsert(self, chunks: list[dict], vectors: list[list[float]]) -> None:
        """按对应日卡填写；当前未实现。"""
        raise NotImplementedError("请按当天任务卡完成 upsert")

    def query(self, vector: list[float], k: int = 3) -> list[dict]:
        """按对应日卡填写；当前未实现。"""
        raise NotImplementedError("请按当天任务卡完成 query")

    def count(self) -> int:
        """按对应日卡填写；当前未实现。"""
        raise NotImplementedError("请按当天任务卡完成 count")

    def close(self) -> None:
        """按对应日卡填写；当前未实现。"""
        raise NotImplementedError("请按当天任务卡完成 close")

