import unittest
import sys
import os

curr_dir = os.path.dirname(__name__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P3908 import Solution

class Testing(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.validDigit(123, 3), True)
    self.assertEqual(self.solution.validDigit(123, 1), False)
    self.assertEqual(self.solution.validDigit(123, 9), False)

if __name__ == "__main__":
  unittest.main()
