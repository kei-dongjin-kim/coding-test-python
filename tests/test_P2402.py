import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P2402 import Solution

class TestP2402(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.mostBooked(3, [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10]]), 0)

if __name__ == "__main__":
  unittest.main()