"""LC 438 找到字符串中所有字母异位词
题目：https://leetcode.cn/problems/find-all-anagrams-in-a-string/
重点：理解固定长度窗口与字符频数比较，覆盖重叠答案。
复杂度目标：时间 O(n + m)，固定字母表空间 O(1)
只实现下面的 TODO；先在纸上写思路、边界和复杂度。
"""

from collections import defaultdict
from typing import Any, Optional, List, Dict, Tuple
from algorithms.interview._structures import ListNode, TreeNode, Node


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:

        m = len(s)
        n = len(p)
        if m<n:
            return []
        d_p = defaultdict(int)
        d_s = defaultdict(int)

        left = 0
        right = n-1
        ans=[]
        for i in range(n):
            d_p[p[i]]+=1
            d_s[s[i]]+=1
        if d_p==d_s:
            ans.append(0)
        
        for right in range(n,m):
            d_s[s[right]]+=1

            d_s[s[left]]-=1
            if d_s[s[left]]==0:
                del d_s[s[left]]
            left+=1

            if d_p == d_s:
                ans.append(left)
        return ans
