import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P2923 import Solution

class TestP2923(unittest.TestCase):
  def setUp(self):
    self.solution = Solution()
  
  def test1(self):
    self.assertEqual(self.solution.findChampion([[0, 1, 0], [0, 0, 1], [1, 1, 0]]), 2)

if __name__ == "__main__":
  unittest.main()
