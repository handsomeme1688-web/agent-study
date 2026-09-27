"""Fixed local cases for LC 169; run LeetCode after these pass."""

import importlib
import json
import unittest
from algorithm_tests.interview._support import run_case

SPEC = json.loads('{"id": 169, "kind": "function", "method": "majorityElement", "returns": "int", "cases": [{"args": [[3, 2, 3]], "expected": 3}, {"args": [[2, 2, 1, 1, 1, 2, 2]], "expected": 2}, {"args": [[1]], "expected": 1}]}')
MODULE = importlib.import_module('algorithms.interview.lc0169_majority_element')


class LC0169Tests(unittest.TestCase):
    def test_case_01(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][0])

    def test_case_02(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][1])

    def test_case_03(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][2])


if __name__ == "__main__":
    unittest.main()
