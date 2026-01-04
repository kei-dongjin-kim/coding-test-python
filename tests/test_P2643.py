import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P2643 import Solution

class TestP2643(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.rowAndMaximumOnes([[0, 0, 0], [0, 0, 1], [0, 1, 1]]), [2, 2])

if __name__ == "__main__":
  unittest.main()