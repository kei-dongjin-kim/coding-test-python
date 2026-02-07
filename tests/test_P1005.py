import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P1005 import Solution

class Testing(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.largestSumAfterKNegations([-3, -2 , -1, 0, 1, 2, 3], 5), 12)

if __name__ == "__main__":
  unittest.main()
