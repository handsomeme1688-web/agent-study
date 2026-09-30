"""LC 15 三数之和
题目：https://leetcode.cn/problems/3sum/
重点：覆盖重复元素、重复解和无解情况，解释去重条件。
复杂度目标：时间 O(n²)，辅助空间取决于排序实现，不计结果
只实现下面的 TODO；先在纸上写思路、边界和复杂度。
"""

from typing import Any, Optional, List, Dict, Tuple
from algorithms.interview._structures import ListNode, TreeNode, Node


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n):
            if nums[i]>0:
                break
            if i>0 and nums[i] ==nums[i-1]:
                continue
            left = i+1
            right = n-1
            while left<right:
                sum = nums[i]+nums[left]+nums[right]
                if sum == 0:
                    result.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1   
                    left+=1
                    right-=1                 
                elif sum<0:
                    left += 1
                else:
                    right -= 1

        return result
