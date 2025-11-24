import unittest
import sys
import os

curr_dir = os.path.dirname(__name__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P3330 import Solution

class TestP3330:
  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.possibleStringCount("aaabbbccc"), 7)

if __name__ == "__main__":
  unittest.main()
