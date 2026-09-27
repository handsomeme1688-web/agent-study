"""LC 1 两数之和
题目：https://leetcode.cn/problems/two-sum/
重点：区分索引与数值，不能重复使用同一元素。
复杂度目标：时间 O(n)，空间 O(n)
只实现下面的 TODO；先在纸上写思路、边界和复杂度。
"""

from typing import Any, Optional, List, Dict, Tuple
from algorithms.interview._structures import ListNode, TreeNode, Node


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d=dict()
        for i, num in enumerate(nums):
            if target-num in d:
                return [d[target-num], i]
            else:
                d[num] = i
        return []

