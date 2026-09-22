import unittest
from algorithms.d02_two_sum_rewrite import solve

class TestAlgorithmD02(unittest.TestCase):
    def test_minimum_example(self):
        self.assertEqual(solve([3, 3], 6), [0, 1])

    # 自己再添加两个非重复边界，最小样例通过不代表算法整体完成。

if __name__ == "__main__":
    unittest.main()
