"""LC 3 无重复字符的最长子串
题目：https://leetcode.cn/problems/longest-substring-without-repeating-characters/
重点：明确窗口内无重复条件，左边界不能倒退。
复杂度目标：时间 O(n)，空间 O(字符集大小)
只实现下面的 TODO；先在纸上写思路、边界和复杂度。
"""

from typing import Any, Optional, List, Dict, Tuple
from algorithms.interview._structures import ListNode, TreeNode, Node


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        max_s = set()
        ans = 0
        for right in range(n):
            while s[right] in max_s:
                max_s.remove(s[left])
                left+=1
            max_s.add(s[right])
            ans = max(ans, right-left+1)
        return ans
