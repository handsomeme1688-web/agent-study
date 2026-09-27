import unittest
from algorithms.d03_valid_parentheses import solve

class TestAlgorithmD03(unittest.TestCase):
    def test_minimum_example(self):
        self.assertEqual(solve("()[]{}"), True)

    # 自己再添加两个非重复边界，最小样例通过不代表算法整体完成。

if __name__ == "__main__":
    unittest.main()
