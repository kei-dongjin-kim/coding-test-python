import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P2161 import Solution

class Testing(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.pivotArray([1, 2, 3, 4, 5], 3), [1, 2, 3, 4, 5])
    self.assertEqual(self.solution.pivotArray([2, 1, 3, 5, 4], 3), [2, 1, 3, 5, 4])

if __name__ == "__main__":
  unittest.main()