"""Fixed local cases for LC 189; run LeetCode after these pass."""

import importlib
import json
import unittest
from algorithm_tests.interview._support import run_case

SPEC = json.loads('{"id": 189, "kind": "function", "method": "rotate", "returns": "None", "cases": [{"args": [[1, 2, 3, 4, 5, 6, 7], 3], "expected": [5, 6, 7, 1, 2, 3, 4], "in_place_arg": 0}, {"args": [[-1, -100, 3, 99], 2], "expected": [3, 99, -1, -100], "in_place_arg": 0}, {"args": [[1, 2], 4], "expected": [1, 2], "in_place_arg": 0}]}')
MODULE = importlib.import_module('algorithms.interview.lc0189_rotate_array')


class LC0189Tests(unittest.TestCase):
    def test_case_01(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][0])

    def test_case_02(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][1])

    def test_case_03(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][2])


if __name__ == "__main__":
    unittest.main()
