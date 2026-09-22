class BudgetExceeded(RuntimeError):
    """达到预算上限。"""

class Budget:
    def __init__(self, max_steps=4, max_requests=5, max_tools=3) -> None:
        """按对应日卡填写；当前未实现。"""
        raise NotImplementedError("请按当天任务卡完成 __init__")

    def take_step(self) -> None:
        """按对应日卡填写；当前未实现。"""
        raise NotImplementedError("请按当天任务卡完成 take_step")

    def take_request(self) -> None:
        """按对应日卡填写；当前未实现。"""
        raise NotImplementedError("请按当天任务卡完成 take_request")

    def take_tool(self) -> None:
        """按对应日卡填写；当前未实现。"""
        raise NotImplementedError("请按当天任务卡完成 take_tool")

    def snapshot(self) -> dict:
        """按对应日卡填写；当前未实现。"""
        raise NotImplementedError("请按当天任务卡完成 snapshot")

