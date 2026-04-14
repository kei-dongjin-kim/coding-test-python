import unittest
import sys
import os

curr_dir = os.path.dirname(__name__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P3898 import Solution

class Testing(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.findDegrees([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [6, 15, 24])

if __name__ == "__main__":
  unittest.main()
