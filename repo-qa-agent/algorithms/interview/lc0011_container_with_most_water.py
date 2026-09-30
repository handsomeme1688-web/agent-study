"""LC 11 盛最多水的容器
题目：https://leetcode.cn/problems/container-with-most-water/
重点：解释面积受什么限制，缩小候选区间为什么不会漏解。
复杂度目标：时间 O(n)，空间 O(1)
只实现下面的 TODO；先在纸上写思路、边界和复杂度。
"""

from typing import Any, Optional, List, Dict, Tuple
from algorithms.interview._structures import ListNode, TreeNode, Node


class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height)-1
        max_area = 0
        while left<right:
            if height[left]<height[right]:
                max_area = max(max_area,height[left]*(right-left))
                left += 1
            else:
                max_area = max(max_area,height[right]*(right-left))
                right -= 1
        return max_area
