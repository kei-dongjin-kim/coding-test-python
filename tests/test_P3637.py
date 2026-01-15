import unittest
import sys
import os

curr_dir = os.path.dirname(__name__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P3637 import Solution

class TestP3637(unittest.TestCase):
  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.isTrionic([1, 2, 3, 2, 1, 2, 3, 4, 5]), True)

if __name__ == "__main__":
  unittest.main()