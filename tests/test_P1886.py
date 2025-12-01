import unittest
import sys
import os

curr_dir = os.path.dirname(__name__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P1886 import Solution

class TestP1886(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertTrue(self.solution.findRotation([[1, 1, 1], [0, 0, 0], [0, 0, 0]], [[0, 0, 1], [0, 0, 1], [0, 0, 1]]))

if __name__ == "__main__":
  unittest.main()