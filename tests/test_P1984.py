import unittest
import sys
import os

curr_dir = os.path.dirname(__name__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P1984 import Solution

class TestP1984(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()
  
  def test1(self):
    self.assertEqual(self.solution.minimumDifference([-5, 0, 3, 10, 15, 20], 2), 3)

if __name__ == "__main__":
  unittest.main()
