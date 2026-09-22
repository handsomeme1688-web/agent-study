class SessionStore:
    def __init__(self, db_path: str) -> None:
        """按对应日卡填写；当前未实现。"""
        raise NotImplementedError("请按当天任务卡完成 __init__")

    def create_session(self, owner_id: str) -> str:
        """按对应日卡填写；当前未实现。"""
        raise NotImplementedError("请按当天任务卡完成 create_session")

    def append_pair(self, session_id: str, question: str, answer: str) -> None:
        """按对应日卡填写；当前未实现。"""
        raise NotImplementedError("请按当天任务卡完成 append_pair")

    def list_messages(self, session_id: str) -> list[dict]:
        """按对应日卡填写；当前未实现。"""
        raise NotImplementedError("请按当天任务卡完成 list_messages")

    def get_owner(self, session_id: str) -> str | None:
        """按对应日卡填写；当前未实现。"""
        raise NotImplementedError("请按当天任务卡完成 get_owner")

