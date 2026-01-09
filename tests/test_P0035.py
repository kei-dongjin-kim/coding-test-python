import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P0035 import Solution

class TestP0035(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.searchInsert([0, 2, 4, 6, 8, 10], 5), 3)
  
  if __name__ == "__main__":
    unittest.main()
