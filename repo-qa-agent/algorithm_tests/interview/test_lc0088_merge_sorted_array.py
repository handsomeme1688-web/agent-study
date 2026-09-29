"""Fixed local cases for LC 88; run LeetCode after these pass."""

import importlib
import json
import unittest
from algorithm_tests.interview._support import run_case

SPEC = json.loads('{"id": 88, "kind": "function", "method": "merge", "returns": "None", "cases": [{"args": [[1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3], "expected": [1, 2, 2, 3, 5, 6], "in_place_arg": 0}, {"args": [[1], 1, [], 0], "expected": [1], "in_place_arg": 0}, {"args": [[0], 0, [1], 1], "expected": [1], "in_place_arg": 0}]}')
MODULE = importlib.import_module('algorithms.interview.lc0088_merge_sorted_array')


class LC0088Tests(unittest.TestCase):
    def test_case_01(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][0])

    def test_case_02(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][1])

    def test_case_03(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][2])


if __name__ == "__main__":
    unittest.main()
