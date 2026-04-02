import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P1725 import Solution

class Testing(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()
  
  def test1(self):
    self.assertEqual(self.solution.countGoodRectangles([[7,10],[3,10],[5,10],[10,7]]), 2)

if __name__ == "__main__":
  unittest.main()
