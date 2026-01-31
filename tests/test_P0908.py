import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P0908 import Solution

class TestP0908(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.smallestRangeI([1, 2, 3, 4, 5, 6, 7], 2), 2)

if __name__ == "__main__":
  unittest.main()
