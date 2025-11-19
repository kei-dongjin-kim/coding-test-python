import unittest
import sys
import os

curr_dir = os.path.dirname(__name__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P3396 import Solution

class TestP3396(unittest.TestCase):
  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.minimumOperations([1, 1, 2, 2, 3, 3, 4, 5]), 2)

if __name__ == "__main__":
  unittest.main()