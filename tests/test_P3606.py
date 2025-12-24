import unittest
import sys
import os

curr_dir = os.path.dirname(__name__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P3606 import Solution

class TestP3606(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.validateCoupons(["TEST3", "TEST#2", "TEST1", "TEST4"], ["grocery", "grocery", "electronics", "wrong"], [True, False, True, True]), ["TEST1", "TEST3"])

if __name__ == "__main__":
  unittest.main()