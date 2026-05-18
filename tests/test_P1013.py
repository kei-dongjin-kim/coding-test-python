import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P1013 import Solution

class Testing(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertTrue(self.solution.canThreePartsEqualSum([0, 0, 0]))
    self.assertTrue(self.solution.canThreePartsEqualSum([1, 1, 1]))
    self.assertTrue(self.solution.canThreePartsEqualSum([3, 1, 2, 3]))

if __name__ == "__main__":
  unittest.main()
