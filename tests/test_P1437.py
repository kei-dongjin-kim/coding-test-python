import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P1437 import Solution

class TestP1437(unittest.TestCase):
  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.kLengthApart([0, 1, 0, 0, 0, 1, 0, 0, 1, 0], 2), True)

if __name__ == "__name__":
  unittest.main()
