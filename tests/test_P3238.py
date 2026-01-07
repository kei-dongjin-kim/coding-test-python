import unittest
import sys
import os

curr_dir = os.path.dirname(__name__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P3238 import Solution

class TestP3238(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.winningPlayerCount(10, [[1,2],[2,1],[2,1],[2,1],[3,2],[3,2],[3,2],[4,3],[5,4]]), 1)

if __name__ == "__main__":
  unittest.main()
