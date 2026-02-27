import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P1619 import Solution

class Testing(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()
  
  def test1(self):
    self.assertEqual(self.solution.trimMean([1,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,10]), 5.00000)

if __name__ == "__main__":
  unittest.main()
