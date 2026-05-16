import unittest
import sys
import os

curr_dir = os.path.dirname(__name__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P3407 import Solution

class Testing(unittest.TestCase):
  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertTrue(self.solution.hasMatch("abcde", "ab*de"))

if __name__ == "__main__":
  unittest.main()