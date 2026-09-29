"""LC 977 有序数组的平方
题目：https://leetcode.cn/problems/squares-of-a-sorted-array/
重点：负数平方改变顺序，说明如何利用原数组有序性。
复杂度目标：时间 O(n)，空间 O(n) 含结果
只实现下面的 TODO；先在纸上写思路、边界和复杂度。
"""

from typing import Any, Optional, List, Dict, Tuple
from algorithms.interview._structures import ListNode, TreeNode, Node


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left = 0
        n = len(nums)
        right = n-1
        tail = n-1
        sq_list = [0]*n
        while left<=right:
            sq_left = nums[left]*nums[left]
            sq_right = nums[right]*nums[right]
            if sq_left < sq_right:
                sq_list[tail]=sq_right
                right-=1
            else:
                sq_list[tail]= sq_left
                left+=1
            tail-=1
        return sq_list
