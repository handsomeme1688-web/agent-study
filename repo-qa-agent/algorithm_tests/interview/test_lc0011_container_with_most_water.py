"""Fixed local cases for LC 11; run LeetCode after these pass."""

import importlib
import json
import unittest
from algorithm_tests.interview._support import run_case

SPEC = json.loads('{"id": 11, "kind": "function", "method": "maxArea", "returns": "int", "cases": [{"args": [[1, 8, 6, 2, 5, 4, 8, 3, 7]], "expected": 49}, {"args": [[1, 1]], "expected": 1}, {"args": [[4, 3, 2, 1, 4]], "expected": 16}]}')
MODULE = importlib.import_module('algorithms.interview.lc0011_container_with_most_water')


class LC0011Tests(unittest.TestCase):
    def test_case_01(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][0])

    def test_case_02(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][1])

    def test_case_03(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][2])


if __name__ == "__main__":
    unittest.main()
