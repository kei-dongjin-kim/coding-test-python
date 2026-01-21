import unittest
import sys
import os

curr_dir = os.path.dirname(__name__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P3314 import Solution

class TestP3314(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.minBitwiseArray([2, 3, 5, 7, 11, 13, 31]), [-1, 1, 4, 3, 9, 12, 15])

if __name__ == "__main__":
  unittest.main()
