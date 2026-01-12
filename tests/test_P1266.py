import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P1266 import Solution
from UserDefinedDataType import TreeNode

class TestP1266(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.minTimeToVisitAllPoints([[0, 0], [3, 10], [-10, 70]]), 70)

if __name__ == "__name__":
  unittest.main()
