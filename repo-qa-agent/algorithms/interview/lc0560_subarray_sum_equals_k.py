"""LC 560 和为 K 的子数组
题目：https://leetcode.cn/problems/subarray-sum-equals-k/
重点：存在负数时普通滑动窗口为何失效；注意空前缀与重复前缀。
复杂度目标：时间 O(n)，空间 O(n)
只实现下面的 TODO；先在纸上写思路、边界和复杂度。
"""

from collections import defaultdict
from typing import Any, Optional, List, Dict, Tuple
from algorithms.interview._structures import ListNode, TreeNode, Node

# 前缀和
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        d=defaultdict(int)
        d[0]=1
        cur_sum = 0
        count = 0 
        for num in nums:
            cur_sum+=num
            count += d[cur_sum-k]
            d[cur_sum]+=1
        return count

