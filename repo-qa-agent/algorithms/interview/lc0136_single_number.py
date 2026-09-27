"""LC 136 只出现一次的数字
题目：https://leetcode.cn/problems/single-number/
重点：利用恰有一个元素一次、其余两次的前提，解释运算性质。
复杂度目标：时间 O(n)，空间 O(1)
只实现下面的 TODO；先在纸上写思路、边界和复杂度。
"""

from typing import Any, Optional, List, Dict, Tuple
from algorithms.interview._structures import ListNode, TreeNode, Node


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # nums.sort()
        # left = right = 0
        
        # n= len(nums)
        # while right<n:
        #     right = left+1
        #     if right<n and nums[left]==nums[right]:
        #         left+=2
        #     else:
        #         return nums[left]

        # 异或运算
        # 1. 任何数与自身异或，结果都为 0
        # 2. 任何数与 0 异或，结果仍为其本身
        # 3. 运算顺序不影响最终结果
        res = 0
        for num in nums:
            res = res^num
        return res 
