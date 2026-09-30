"""Fixed local cases for LC 42; run LeetCode after these pass."""

import importlib
import json
import unittest
from algorithm_tests.interview._support import run_case

SPEC = json.loads('{"id": 42, "kind": "function", "method": "trap", "returns": "int", "cases": [{"args": [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]], "expected": 6}, {"args": [[4, 2, 0, 3, 2, 5]], "expected": 9}, {"args": [[1, 2, 3]], "expected": 0}]}')
MODULE = importlib.import_module('algorithms.interview.lc0042_trapping_rain_water')


class LC0042Tests(unittest.TestCase):
    def test_case_01(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][0])

    def test_case_02(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][1])

    def test_case_03(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][2])


if __name__ == "__main__":
    unittest.main()
