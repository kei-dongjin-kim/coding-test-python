import unittest
import sys
import os

curr_dir = os.path.dirname(__name__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P3917 import Solution

class Testing(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.countOppositeParity([0, 1, 2, 3, 4]), [2, 2, 1, 1, 0])

if __name__ == "__main__":
  unittest.main()
