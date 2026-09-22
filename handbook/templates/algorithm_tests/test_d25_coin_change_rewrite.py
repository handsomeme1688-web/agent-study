import unittest
from algorithms.d25_coin_change_rewrite import solve

class TestAlgorithmD25(unittest.TestCase):
    def test_minimum_example(self):
        self.assertEqual(solve([2], 3), -1)

    # 自己再添加两个非重复边界，最小样例通过不代表算法整体完成。

if __name__ == "__main__":
    unittest.main()
