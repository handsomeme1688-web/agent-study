"""Fixed local cases for LC 438; run LeetCode after these pass."""

import importlib
import json
import unittest
from algorithm_tests.interview._support import run_case

SPEC = json.loads('{"id": 438, "kind": "function", "method": "findAnagrams", "returns": "list[int]", "cases": [{"args": ["cbaebabacd", "abc"], "expected": [0, 6], "comparator": "unordered"}, {"args": ["abab", "ab"], "expected": [0, 1, 2], "comparator": "unordered"}, {"args": ["a", "ab"], "expected": [], "comparator": "unordered"}]}')
MODULE = importlib.import_module('algorithms.interview.lc0438_find_all_anagrams_in_a_string')


class LC0438Tests(unittest.TestCase):
    def test_case_01(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][0])

    def test_case_02(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][1])

    def test_case_03(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][2])


if __name__ == "__main__":
    unittest.main()
