"""Fixed local cases for LC 3; run LeetCode after these pass."""

import importlib
import json
import unittest
from algorithm_tests.interview._support import run_case

SPEC = json.loads('{"id": 3, "kind": "function", "method": "lengthOfLongestSubstring", "returns": "int", "cases": [{"args": ["abcabcbb"], "expected": 3}, {"args": [""], "expected": 0}, {"args": ["abba"], "expected": 2}]}')
MODULE = importlib.import_module('algorithms.interview.lc0003_longest_substring_without_repeating_characters')


class LC0003Tests(unittest.TestCase):
    def test_case_01(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][0])

    def test_case_02(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][1])

    def test_case_03(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][2])


if __name__ == "__main__":
    unittest.main()
