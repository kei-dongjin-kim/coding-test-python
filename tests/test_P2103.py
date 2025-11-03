import unittest
import sys
import os

current_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(current_dir, "..", "src"))
sys.path.append(src_dir)

from P2103 import Solution

class TestP2103(unittest.TestCase):
  def setUp(self):
    self.solution = Solution()
  
  def test1(self):
    rings = "R0G0B0R1G1B1R2G2B2"
    self.assertEqual(self.solution.countPoints(rings), 3)

if __name__ == "__main__":
  unittest.main()
