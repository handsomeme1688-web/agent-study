"""LC 42 接雨水
题目：https://leetcode.cn/problems/trapping-rain-water/
重点：理解每处水位受左右边界共同限制，区分容器面积。
复杂度目标：目标时间 O(n)，额外空间 O(1)；先允许 O(n) 空间
只实现下面的 TODO；先在纸上写思路、边界和复杂度。
"""

from typing import Any, Optional, List, Dict, Tuple
from algorithms.interview._structures import ListNode, TreeNode, Node


class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        left_max = 0
        right_max = 0
        ans = 0
        while left<right:
            left_max=max(left_max,height[left])
            right_max=max(right_max,height[right])
            if left_max<right_max:
                ans += left_max-height[left]
                left+=1
            else :
                ans+= right_max-height[right]
                right-=1
        return ans
