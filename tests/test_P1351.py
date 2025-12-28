import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P1351 import Solution

class TestP1351(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.countNegatives([[5, 4, 3, 2, 1], [1, 0, -1, -2, -3], [-1, -2, -3, -4, -5], [-2, -3, -4, -5, -6], [-3, -4, -5, -6, -7]]), 18)

if __name__ == "__name__":
  unittest.main()
