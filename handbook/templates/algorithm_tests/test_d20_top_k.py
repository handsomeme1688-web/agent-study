import unittest
from algorithms.d20_top_k import solve

class TestAlgorithmD20(unittest.TestCase):
    def test_minimum_example(self):
        self.assertCountEqual(solve([1,1,1,2,2,3], 2), [1,2])

    # 自己再添加两个非重复边界，最小样例通过不代表算法整体完成。

if __name__ == "__main__":
    unittest.main()
