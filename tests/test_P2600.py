import unittest
import sys
import os

current_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(current_dir, "..", "src"))
sys.path.append(src_dir)

from P2600 import Solution

class TestKItemsWithMaximumSum(unittest.TestCase):
  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.kItemsWithMaximumSum(1, 1, 1, 3), 0)

if __name__ == "__main__":
  unittest.main()
