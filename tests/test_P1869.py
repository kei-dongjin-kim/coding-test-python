import unittest
import sys
import os

curr_dir = os.path.dirname(__name__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P1869 import Solution

class TestP1869(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertTrue(self.solution.checkZeroOnes("1010101111"))

if __name__ == "__main__":
  unittest.main()