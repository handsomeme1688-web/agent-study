"""LC 42 接雨水
题目：https://leetcode.cn/problems/trapping-rain-water/
重点：理解每处水位受左右边界共同限制，区分容器面积。
复杂度目标：目标时间 O(n)，额外空间 O(1)；先允许 O(n) 空间
只实现下面的 TODO；先在纸上写思路、边界和复杂度。
"""

from typing import Any, Optional, List, Dict, Tuple
from algorithms.interview._structures import ListNode, TreeNode, Node

'''
在接雨水时本能的想法是：找波谷、算水坑、大面积减初始面积。这是“面”的视角。
微观/点视角（破局关键）：把总收益拆分成每个元素的独立收益

抓住双指针的核心支柱：“单调性”与“无悔排除”
双指针不是靠“猜”哪边该动，它的数学本质是搜索空间的无悔剪枝

建立“三问解题闭环”:
    1. 目标计算单元是什么？
    2. 影响当前单元答案的极限约束是什么？
    3. 怎样利用单边信息做决策？
'''
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
