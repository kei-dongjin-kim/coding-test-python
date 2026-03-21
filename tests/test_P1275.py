import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P1275 import Solution

class Testing(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    moves = [[1, 1], [0, 0], [0, 1], [1, 0], [2, 1]]
    self.assertEqual(self.solution.tictactoe(moves), "A")

if __name__ == "__main__":
  unittest.main()
