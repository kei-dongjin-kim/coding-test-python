import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P1232 import Solution

class TestP1232(unittest.TestCase):
  def setUp(self):
    self.solution = Solution()

  def test1(self):
    coords = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
    self.assertTrue(self.solution.checkStraightLine(coords))

if __name__ == "__main__":
  unittest.main()
