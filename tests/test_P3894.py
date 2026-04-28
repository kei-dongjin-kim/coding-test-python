import unittest
import sys
import os

curr_dir = os.path.dirname(__name__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P3894 import Solution

class Testing(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.trafficSignal(0), "Green")
    self.assertEqual(self.solution.trafficSignal(30), "Orange")
    self.assertEqual(self.solution.trafficSignal(60), "Red")
    self.assertEqual(self.solution.trafficSignal(100), "Invalid")

if __name__ == "__main__":
  unittest.main()
