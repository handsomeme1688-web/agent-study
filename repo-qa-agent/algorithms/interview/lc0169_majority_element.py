"""LC 169 多数元素
题目：https://leetcode.cn/problems/majority-element/
重点：题目保证多数元素存在；严格超过一半与出现最多不同。
复杂度目标：目标时间 O(n)，空间 O(1)
只实现下面的 TODO；先在纸上写思路、边界和复杂度。
"""

from collections import defaultdict
from typing import Any, Optional, List, Dict, Tuple
from algorithms.interview._structures import ListNode, TreeNode, Node


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # count = defaultdict(int)
        # for num in nums:
        #     count[num]+=1
        # for key, value in count.items():
        #     if value > int(len(nums)/2):
        #         return key


        # 最优解：摩尔投票法, o(N),o(1)
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count+=1
            else:
                count-=1
        return candidate


'''
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
'''



