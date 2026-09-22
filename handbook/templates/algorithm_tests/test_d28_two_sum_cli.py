import unittest
from algorithms.d28_two_sum_cli import solve

class TestAlgorithmD28(unittest.TestCase):
    def test_minimum_example(self):
        self.assertEqual(solve([2,7,11,15], 9), [0,1])

    # 自己再添加两个非重复边界，最小样例通过不代表算法整体完成。

if __name__ == "__main__":
    unittest.main()
