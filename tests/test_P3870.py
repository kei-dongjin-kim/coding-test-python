import unittest
import sys
import os

curr_dir = os.path.dirname(__name__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P3870 import Solution

class Testing(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.countCommas(999), 0)
    self.assertEqual(self.solution.countCommas(1000), 1)
    self.assertEqual(self.solution.countCommas(1001), 2)
    self.assertEqual(self.solution.countCommas(1010), 11)
    self.assertEqual(self.solution.countCommas(5000), 4001)

if __name__ == "__main__":
  unittest.main()
