import unittest
from algorithms.d01_two_sum import solve

class TestAlgorithmD01(unittest.TestCase):
    def test_minimum_example(self):
        self.assertEqual(solve([2, 7, 11, 15], 9), [0, 1])

    def test_same_value_twice(self):
        """同一个值出现两次：不能用同一个下标两次"""
        self.assertEqual(solve([3, 3], 6), [0, 1])

    def test_pair_found_late(self):
        """经典陷阱：先查后登记，不能返回 [0, 0]"""
        self.assertEqual(solve([3, 2, 4], 6), [1, 2])

    # 自己再添加两个非重复边界，最小样例通过不代表算法整体完成。

if __name__ == "__main__":
    unittest.main()
