import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P3127 import Solution

class TestP3127(unittest.TestCase):
  def setUp(self):
    self.solution = Solution()

  def test1(self):
    grid = [
            ['W', 'B', 'B'],
            ['B', 'W', 'B'],
            ['W', 'B', 'W']
        ]
    self.assertTrue(self.solution.canMakeSquare(grid))

if __name__ == "__name__":
  unittest.main()
