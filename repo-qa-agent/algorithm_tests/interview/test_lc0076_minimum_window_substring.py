"""Fixed local cases for LC 76; run LeetCode after these pass."""

import importlib
import json
import unittest
from algorithm_tests.interview._support import run_case

SPEC = json.loads('{"id": 76, "kind": "function", "method": "minWindow", "returns": "str", "cases": [{"args": ["ADOBECODEBANC", "ABC"], "expected": "BANC"}, {"args": ["a", "aa"], "expected": ""}, {"args": ["aa", "aa"], "expected": "aa"}]}')
MODULE = importlib.import_module('algorithms.interview.lc0076_minimum_window_substring')


class LC0076Tests(unittest.TestCase):
    def test_case_01(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][0])

    def test_case_02(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][1])

    def test_case_03(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][2])


if __name__ == "__main__":
    unittest.main()
