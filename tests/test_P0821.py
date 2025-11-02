import unittest
import sys
import os

current_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(current_dir, "..", "src"))
sys.path.append(src_dir)

from P0821 import Solution

class TestP0821(unittest.TestCase):
  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.shortestToChar("abcde", "e"), [4, 3, 2, 1, 0])

if __name__ == "__main__":
  unittest.main()
