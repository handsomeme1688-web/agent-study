import unittest
from algorithms.d02_two_sum_rewrite import solve

class TestAlgorithmD02(unittest.TestCase):
    def test_minimum_example(self):
        self.assertEqual(solve([3, 3], 6), [0, 1])

    def test_no_self_pairing(self):
        """经典陷阱：先查后登记，不能返回 [0, 0]（答案不含重复值，但错误实现仍会自配）"""
        self.assertEqual(solve([3, 2, 4], 6), [1, 2])

    def test_no_solution(self):
        """无解：走到最后返回空列表，测 return [] 这个防御分支"""
        self.assertEqual(solve([1, 2], 100), [])

if __name__ == "__main__":
    unittest.main()
