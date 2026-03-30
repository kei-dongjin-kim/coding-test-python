import unittest
import sys
import os

curr_dir = os.path.dirname(__name__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P3884 import Solution

class Testing(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.firstMatchingIndex("abcdefga"), 0)
    self.assertEqual(self.solution.firstMatchingIndex("abcdefg"), 3)
    self.assertEqual(self.solution.firstMatchingIndex("aaaaaaaa"), 0)
    self.assertEqual(self.solution.firstMatchingIndex("abcabc"), 1)

if __name__ == "__main__":
  unittest.main()
