import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P2639 import Solution

class Testing(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.findColumnWidth([[0, 0, 11111], [0, 1111, 0], [111, 0, 0]]), [3, 4, 5])

if __name__ == "__main__":
  unittest.main()