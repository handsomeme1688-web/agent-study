"""LC 209 长度最小的子数组
题目：https://leetcode.cn/problems/minimum-size-subarray-sum/
重点：明确正整数前提，区分满足目标与最短窗口，覆盖无解。
复杂度目标：时间 O(n)，空间 O(1)
只实现下面的 TODO；先在纸上写思路、边界和复杂度。
"""

from typing import Any, Optional, List, Dict, Tuple
from algorithms.interview._structures import ListNode, TreeNode, Node


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        left = 0
        cur_sum = 0
        ans = n+1
        for right in range(n):
            cur_sum += nums[right]
            while cur_sum >= target :
                ans = min(ans,right-left+1)
                cur_sum-=nums[left]
                left+=1
        return ans if ans<=n else 0

            
                


        
