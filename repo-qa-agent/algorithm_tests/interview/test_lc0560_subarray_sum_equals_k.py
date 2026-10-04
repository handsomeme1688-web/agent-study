"""Fixed local cases for LC 560; run LeetCode after these pass."""

import importlib
import json
import unittest
from algorithm_tests.interview._support import run_case

SPEC = json.loads('{"id": 560, "kind": "function", "method": "subarraySum", "returns": "int", "cases": [{"args": [[1, 1, 1], 2], "expected": 2}, {"args": [[1, -1, 0], 0], "expected": 3}, {"args": [[0, 0, 0], 0], "expected": 6}]}')
MODULE = importlib.import_module('algorithms.interview.lc0560_subarray_sum_equals_k')


class LC0560Tests(unittest.TestCase):
    def test_case_01(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][0])

    def test_case_02(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][1])

    def test_case_03(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][2])


if __name__ == "__main__":
    unittest.main()
