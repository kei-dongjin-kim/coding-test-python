import unittest
import sys
import os

curr_dir = os.path.dirname(__name__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P1909 import Solution

class Testing(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()
  
  def test1(self):
    self.assertEqual(self.solution.canBeIncreasing([1, 2, 10, 3, 4]), True)

  def test2(self):
    self.assertEqual(self.solution.canBeIncreasing([1, 2, 0, 3, 4]), True)

  def test3(self):
    self.assertEqual(self.solution.canBeIncreasing([1, 2, 3, 4, 0]), True)

  def test4(self):
    self.assertEqual(self.solution.canBeIncreasing([10, 1, 2, 3, 4]), True)

if __name__ == "__main__":
  unittest.main()
