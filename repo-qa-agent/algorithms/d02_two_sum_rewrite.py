"""D02：两数之和闭卷。函数名在本地统一为solve。"""

def solve(nums: list[int], target: int) -> list[int]:
    """自己实现，不复制前一天答案；再补两个边界测试。"""
    d=dict()
    for i, num in enumerate(nums):
        if target-num in d:
            return [d[target-num],i]
        else:
            d[num] = i
    return []

    # raise NotImplementedError("请按当天任务卡完成 solve")

