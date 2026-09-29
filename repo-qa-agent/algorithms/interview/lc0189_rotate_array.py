"""LC 189 轮转数组
题目：https://leetcode.cn/problems/rotate-array/
重点：覆盖 k 大于数组长度、k 为零以及原地操作的边界。
复杂度目标：时间 O(n)，目标额外空间 O(1)
只实现下面的 TODO；先在纸上写思路、边界和复杂度。
"""

from typing import Any, Optional, List, Dict, Tuple
from algorithms.interview._structures import ListNode, TreeNode, Node


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n=len(nums)
        k = k%n # k未必小于n
        def reverse(left,right):
            while left<=right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)

            
