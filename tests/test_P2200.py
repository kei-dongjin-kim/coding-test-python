import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P2200 import Solution

class TestP2200(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.findKDistantIndices([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 5, 2), [3, 4, 5, 6, 7])

if __name__ == "__main__":
  unittest.main()