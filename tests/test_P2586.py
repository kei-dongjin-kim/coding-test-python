import unittest
import sys
import os

current_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(current_dir, "..", "src"))
sys.path.append(src_dir)

from P2586 import Solution

class TestVowelStrings(unittest.TestCase):
  def setUp(self):
    self.solution = Solution()

  def test1(self):
    words = ["apple", "banana", "orange", "egg", "umbrella"]
    self.assertEqual(self.solution.vowelStrings(words, 0, 4), 3)

if __name__ == "__main__":
  unittest.main()
