import unittest
from algorithms.d10_binary_search import solve

class TestAlgorithmD10(unittest.TestCase):
    def test_minimum_example(self):
        self.assertEqual(solve([-1,0,3,5,9,12], 9), 4)

    # 自己再添加两个非重复边界，最小样例通过不代表算法整体完成。

if __name__ == "__main__":
    unittest.main()
