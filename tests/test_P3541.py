import unittest
import sys
import os

curr_dir = os.path.dirname(__name__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P3541 import Solution

class Testing(unittest.TestCase):
  def setUp(self):
    self.solution = Solution()
  
  def test1(self):
    self.assertEqual(self.solution.maxFreqSum("testtesttest"), 9)

if __name__ == "__main__":
  unittest.main()
