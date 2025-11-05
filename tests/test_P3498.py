import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P3498 import Solution

class TestP3498(unittest.TestCase):
  def setUp(self):
    self.solution = Solution()
  
  def test1(self):
    # "aaa" → (26-0)*1 + (26-0)*2 + (26-0)*3 = 26 + 52 + 78 = 156
    self.assertEqual(self.solution.reverseDegree("aaa"), 156)

if __name__ == "__main__":
  unittest.main()
