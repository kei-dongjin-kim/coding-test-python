import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P3745 import Solution

class TestP3745(unittest.TestCase):
  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.maximizeExpressionOfThree([1, 2, 3, 4, 5]), 8)

if __name__ == "__main__":
  unittest.main()