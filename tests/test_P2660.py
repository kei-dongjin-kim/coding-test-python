import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P2660 import Solution

class TestP2660(unittest.TestCase):
  def setUp(self):
    self.solution = Solution()

  def test1(self):
    player1 = [10, 10, 1]
    player2 = [10, 5, 5]
    self.assertEqual(self.solution.isWinner(player1, player2), 1)

if __name__ == "__main__":
  unittest.main()
