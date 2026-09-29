"""Fixed local cases for LC 977; run LeetCode after these pass."""

import importlib
import json
import unittest
from algorithm_tests.interview._support import run_case

SPEC = json.loads('{"id": 977, "kind": "function", "method": "sortedSquares", "returns": "list[int]", "cases": [{"args": [[-4, -1, 0, 3, 10]], "expected": [0, 1, 9, 16, 100]}, {"args": [[-7, -3, 2, 3, 11]], "expected": [4, 9, 9, 49, 121]}, {"args": [[-1]], "expected": [1]}]}')
MODULE = importlib.import_module('algorithms.interview.lc0977_squares_of_a_sorted_array')


class LC0977Tests(unittest.TestCase):
    def test_case_01(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][0])

    def test_case_02(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][1])

    def test_case_03(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][2])


if __name__ == "__main__":
    unittest.main()
