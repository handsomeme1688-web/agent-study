"""Fixed local cases for LC 49; run LeetCode after these pass."""

import importlib
import json
import unittest
from algorithm_tests.interview._support import run_case

SPEC = json.loads('{"id": 49, "kind": "function", "method": "groupAnagrams", "returns": "list[list[str]]", "cases": [{"args": [["eat", "tea", "tan", "ate", "nat", "bat"]], "expected": [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]], "comparator": "unordered_nested"}, {"args": [[""]], "expected": [[""]], "comparator": "unordered_nested"}, {"args": [["a", "a", "b"]], "expected": [["a", "a"], ["b"]], "comparator": "unordered_nested"}]}')
MODULE = importlib.import_module('algorithms.interview.lc0049_group_anagrams')


class LC0049Tests(unittest.TestCase):
    def test_case_01(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][0])

    def test_case_02(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][1])

    def test_case_03(self):
        run_case(self, MODULE, SPEC, SPEC['cases'][2])


if __name__ == "__main__":
    unittest.main()
