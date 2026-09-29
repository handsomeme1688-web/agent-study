"""LC 283 移动零
题目：https://leetcode.cn/problems/move-zeroes/
重点：保持非零元素相对顺序，区分原地修改和返回值。
复杂度目标：时间 O(n)，额外空间 O(1)
只实现下面的 TODO；先在纸上写思路、边界和复杂度。
"""

from typing import Any, Optional, List, Dict, Tuple
from algorithms.interview._structures import ListNode, TreeNode, Node


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
                

            

        
