import unittest
import sys
import os

curr_dir = os.path.dirname(__name__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P2595 import Solution

class TestEvenOddBit(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.evenOddBit(0), [0, 0])
        self.assertEqual(self.solution.evenOddBit(10), [0, 2])

if __name__ == "__main__":
    unittest.main()
