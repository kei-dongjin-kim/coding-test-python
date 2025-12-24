import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P3074 import Solution

class TestP3074(unittest.TestCase):
  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertTrue(self.solution.minimumBoxes([10, 10, 10], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]), 6)

if __name__ == "__name__":
  unittest.main()
