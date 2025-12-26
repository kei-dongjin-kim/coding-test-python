import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P2303 import Solution

class TestP2303(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.calculateTax([[10, 10], [20, 10], [30, 10]], 20), 2.0)

if __name__ == "__main__":
  unittest.main()