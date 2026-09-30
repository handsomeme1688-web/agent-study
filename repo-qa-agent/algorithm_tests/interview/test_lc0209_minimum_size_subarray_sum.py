"""Fixed local cases for LC 209; run LeetCode after these pass."""

import importlib
import json
import unittest
from algorithm_tests.interview._support import run_case

SPEC = json.loads('{"id": 209, "kind": "function", "method": "minSubArrayLen", "returns": "int", "cases": [{"args": [7, [2, 3, 1, 2, 4, 3]], "expected": 2}, {"args": [4, [1, 4, 4]], "expected": 1}, {"args": [11, [1, 1, 1, 1, 1, 1, 1, 1]], "expected": 0}]}')
MODULE = importlib.import_module('algorithms.interview.lc0209_minimum_size_subarray_sum')


class LC0209Tests(unittest.TestCase):
    def test_case_01(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][0])

    def test_case_02(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][1])

    def test_case_03(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][2])


if __name__ == "__main__":
    unittest.main()
