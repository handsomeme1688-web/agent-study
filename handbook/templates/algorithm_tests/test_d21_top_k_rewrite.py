import unittest
from algorithms.d21_top_k_rewrite import solve

class TestAlgorithmD21(unittest.TestCase):
    def test_minimum_example(self):
        self.assertCountEqual(solve([1], 1), [1])

    # 自己再添加两个非重复边界，最小样例通过不代表算法整体完成。

if __name__ == "__main__":
    unittest.main()
