import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P0944 import Solution

class TestP0944(unittest.TestCase):
  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertTrue(self.solution.minDeletionSize(["aaa", "bbb", "cca"]), 1)

if __name__ == "__main__":
  unittest.main()
