import unittest
import sys
import os

curr_dir = os.path.dirname(__name__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P3423 import Solution

class TestP3423(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.maxAdjacentDistance([1, 2, 3, 4, 5, 6, 7, 8]), 7)

if __name__ == "__main__":
  unittest.main()