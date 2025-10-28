import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from P1848 import Solution

class TestGetMinDistance(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        nums = [1, 2, 3, 4, 5]
        target = 5
        start = 3
        self.assertEqual(self.solution.getMinDistance(nums, target, start), 1)

if __name__ == "__main__":
    unittest.main()