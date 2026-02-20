import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P2264 import Solution

class Testing(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.largestGoodInteger("1234567778889"), "888")

if __name__ == "__main__":
  unittest.main()