import unittest
import sys
import os

curr_dir = os.path.dirname(__name__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P0541 import Solution

class TestP0541(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.reverseStr("cbadefihgjk", 3), "abcdefghijk")

if __name__ == "__main__":
  unittest.main()