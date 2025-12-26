import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P3075 import Solution

class TestP3075(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertTrue(self.solution.maximumHappinessSum([5, 6, 7, 8, 9], 3), 15)

if __name__ == "__name__":
  unittest.main()
