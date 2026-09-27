"""Fixed local cases for LC 1; run LeetCode after these pass."""

import importlib
import json
import unittest
from algorithm_tests.interview._support import run_case

SPEC = json.loads('{"id": 1, "kind": "function", "method": "twoSum", "returns": "list[int]", "cases": [{"args": [[2, 7, 11, 15], 9], "expected": [0, 1], "comparator": "unordered"}, {"args": [[3, 2, 4], 6], "expected": [1, 2], "comparator": "unordered"}, {"args": [[3, 3], 6], "expected": [0, 1], "comparator": "unordered"}]}')
MODULE = importlib.import_module('algorithms.interview.lc0001_two_sum')


class LC0001Tests(unittest.TestCase):
    def test_case_01(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][0])

    def test_case_02(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][1])

    def test_case_03(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][2])


if __name__ == "__main__":
    unittest.main()
