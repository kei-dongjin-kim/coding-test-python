import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P0892 import Solution

class TestP0892(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.surfaceArea([[2, 2], [2, 2]]), 24)

if __name__ == "__main__":
  unittest.main()
