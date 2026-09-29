"""LC 88 合并两个有序数组
题目：https://leetcode.cn/problems/merge-sorted-array/
重点：nums1 尾部零是预留空间，按 m 识别有效元素，覆盖空侧。
复杂度目标：时间 O(m+n)，额外空间 O(1)
只实现下面的 TODO；先在纸上写思路、边界和复杂度。
"""

from typing import Any, Optional, List, Dict, Tuple
from algorithms.interview._structures import ListNode, TreeNode, Node


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        p1 = m-1
        p2 = n-1
        tail = m+n-1
        while p2>=0:
            if p1>0 and nums1[p1]>nums2[p2]:
                nums1[tail]= nums1[p1]
                p1-=1
            else:
                nums1[tail]=nums2[p2]
                p2-=1
            tail-=1


            

