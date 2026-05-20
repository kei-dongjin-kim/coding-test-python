import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P2657 import Solution

class Testing(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    A = [3, 2, 1, 4]
    B = [1, 2, 3, 4]
    self.assertEqual(self.solution.findThePrefixCommonArray(A, B), [0, 1, 3, 4])

if __name__ == "__main__":
  unittest.main()
