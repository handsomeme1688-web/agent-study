import unittest
from algorithms.d16_islands import solve

class TestAlgorithmD16(unittest.TestCase):
    def test_minimum_example(self):
        self.assertEqual(solve([["1","0"],["0","1"]]), 2)

    # 自己再添加两个非重复边界，最小样例通过不代表算法整体完成。

if __name__ == "__main__":
    unittest.main()
