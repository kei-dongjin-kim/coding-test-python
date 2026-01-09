import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P0011 import Solution

class TestP0011(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.maxArea([1, 2, 3, 7, 5, 6, 7, 8, 9, 10]), 42)
  
  if __name__ == "__main__":
    unittest.main()
