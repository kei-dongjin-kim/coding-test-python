import unittest
import sys
import os

current_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(current_dir, "..", "src"))
sys.path.append(src_dir)

from P2578 import Solution

class Testing(unittest.TestCase):
  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.splitNum(123456789), 16047)

if __name__ == "__main__":
  unittest.main()
