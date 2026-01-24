import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P2833 import Solution

class TestP2833(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()
  
  def test1(self):
    self.assertEqual(self.solution.furthestDistanceFromOrigin("L_RLRRLRLRLRL____"), 5)

if __name__ == "__main__":
  unittest.main()
