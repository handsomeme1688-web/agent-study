import unittest
from algorithms.d14_level_order import solve

class TestAlgorithmD14(unittest.TestCase):
    def test_minimum_example(self):
        self.assertEqual(solve(None), [])

    # 自己再添加两个非重复边界，最小样例通过不代表算法整体完成。

if __name__ == "__main__":
    unittest.main()
