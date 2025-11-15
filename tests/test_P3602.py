import unittest
import sys
import os

curr_dir = os.path.dirname(__name__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P3602 import Solution

class TestP3602(unittest.TestCase):
  def setUp(self):
    self.solution = Solution()
  
  def test1(self):
    self.assertEqual(self.solution.concatHex36(37), "5591331")

if __name__ == "__main__":
  unittest.main()
