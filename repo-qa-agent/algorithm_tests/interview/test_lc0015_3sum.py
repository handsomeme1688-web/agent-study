"""Fixed local cases for LC 15; run LeetCode after these pass."""

import importlib
import json
import unittest
from algorithm_tests.interview._support import run_case

SPEC = json.loads('{"id": 15, "kind": "function", "method": "threeSum", "returns": "list[list[int]]", "cases": [{"args": [[-1, 0, 1, 2, -1, -4]], "expected": [[-1, -1, 2], [-1, 0, 1]], "comparator": "unordered_nested"}, {"args": [[0, 0, 0, 0]], "expected": [[0, 0, 0]], "comparator": "unordered_nested"}, {"args": [[0, 1, 1]], "expected": [], "comparator": "unordered_nested"}]}')
MODULE = importlib.import_module('algorithms.interview.lc0015_3sum')


class LC0015Tests(unittest.TestCase):
    def test_case_01(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][0])

    def test_case_02(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][1])

    def test_case_03(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][2])


if __name__ == "__main__":
    unittest.main()
