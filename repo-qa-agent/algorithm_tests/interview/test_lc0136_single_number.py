"""Fixed local cases for LC 136; run LeetCode after these pass."""

import importlib
import json
import unittest
from algorithm_tests.interview._support import run_case

SPEC = json.loads('{"id": 136, "kind": "function", "method": "singleNumber", "returns": "int", "cases": [{"args": [[2, 2, 1]], "expected": 1}, {"args": [[4, 1, 2, 1, 2]], "expected": 4}, {"args": [[1]], "expected": 1}]}')
MODULE = importlib.import_module('algorithms.interview.lc0136_single_number')


class LC0136Tests(unittest.TestCase):
    def test_case_01(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][0])

    def test_case_02(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][1])

    def test_case_03(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][2])


if __name__ == "__main__":
    unittest.main()
