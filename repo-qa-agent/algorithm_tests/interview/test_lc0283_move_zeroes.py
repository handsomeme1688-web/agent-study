"""Fixed local cases for LC 283; run LeetCode after these pass."""

import importlib
import json
import unittest
from algorithm_tests.interview._support import run_case

SPEC = json.loads('{"id": 283, "kind": "function", "method": "moveZeroes", "returns": "None", "cases": [{"args": [[0, 1, 0, 3, 12]], "expected": [1, 3, 12, 0, 0], "in_place_arg": 0}, {"args": [[0]], "expected": [0], "in_place_arg": 0}, {"args": [[1, 2, 3]], "expected": [1, 2, 3], "in_place_arg": 0}]}')
MODULE = importlib.import_module('algorithms.interview.lc0283_move_zeroes')


class LC0283Tests(unittest.TestCase):
    def test_case_01(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][0])

    def test_case_02(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][1])

    def test_case_03(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][2])


if __name__ == "__main__":
    unittest.main()
