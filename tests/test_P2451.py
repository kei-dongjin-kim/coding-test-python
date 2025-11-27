import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P2451 import Solution

class TestP2451(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.oddString(["abcde", "abcde", "aaaaa"]), "aaaaa")

if __name__ == "__main__":
  unittest.main()
