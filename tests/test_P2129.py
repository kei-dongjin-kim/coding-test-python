import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P2129 import Solution

class Testing(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.capitalizeTitle("abcde fg hi jk lmn opqr"), "Abcde fg hi jk Lmn Opqr")

if __name__ == "__main__":
  unittest.main()