import unittest
import sys
import os

current_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(current_dir, "..", "src"))
sys.path.append(src_dir)

from P0643 import Solution

class TestFindMaxAverage(unittest.TestCase):
  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.findMaxAverage(self.sol.findMaxAverage([3,3,3,3], 4), 3.0)

if __name__ == "__main__":
  unittest.main()