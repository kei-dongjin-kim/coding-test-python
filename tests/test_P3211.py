import unittest
import sys
import os

curr_dir = os.path.dirname(__name__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P3211 import Solution

class Testing(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.validStrings(1), ["0", "1"])
    self.assertEqual(self.solution.validStrings(2), ["01", "10", "11"])
    self.assertEqual(self.solution.validStrings(3), ["010","011","101","110","111"])

if __name__ == "__main__":
  unittest.main()
