"""LC 49 字母异位词分组
题目：https://leetcode.cn/problems/group-anagrams/
重点：分组键应一致且可哈希，覆盖空字符串与重复字符串。
复杂度目标：n 个字符串、最长 k：时间 O(nk log k)；计数键可到 O(nk)
只实现下面的 TODO；先在纸上写思路、边界和复杂度。
"""

from collections import defaultdict
from typing import Any, Optional, List, Dict, Tuple
from algorithms.interview._structures import ListNode, TreeNode, Node


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for word in strs:
            tmp_list = []
            for char in word:
                tmp_list.append(char)
            key_list = sorted(tmp_list)
            key = "".join(char for char in key_list)
            groups[key].append(word)
        return [value for value in groups.values()]
