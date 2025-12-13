import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P2855 import Solution

class TestP2855(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()
  
  def test1(self):
    self.assertEqual(self.solution.minimumRightShifts([5, 1, 2, 3, 4]), 4)

if __name__ == "__main__":
  unittest.main()
