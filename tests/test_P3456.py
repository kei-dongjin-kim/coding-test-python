import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P3456 import Solution

class TestP3456(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()
  
  def test1(self):
    self.assertTrue(self.solution.hasSpecialSubstring("abcdeeefg", 3))

if __name__ == "__main__":
  unittest.main()
