import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P2148 import Solution

class TestP2148(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.countElements([1, 1, 2, 3, 4, 5, 5]), 3)

if __name__ == "__main__":
  unittest.main()