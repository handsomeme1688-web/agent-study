import unittest
from algorithms.d22_house_robber import solve

class TestAlgorithmD22(unittest.TestCase):
    def test_minimum_example(self):
        self.assertEqual(solve([2,7,9,3,1]), 12)

    # 自己再添加两个非重复边界，最小样例通过不代表算法整体完成。

if __name__ == "__main__":
    unittest.main()
