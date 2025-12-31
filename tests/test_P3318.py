import unittest
import sys
import os

curr_dir = os.path.dirname(__name__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P3318 import Solution

class TestP3318(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.findXSum([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 7, 2), [10, 14, 14, 18])

if __name__ == "__main__":
  unittest.main()
