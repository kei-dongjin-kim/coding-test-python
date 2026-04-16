import unittest
import sys
import os

current_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(current_dir, "..", "src"))
sys.path.append(src_dir)

from P2515 import Solution

class Testing(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.closestTarget(["a", "b", "c", "d", "e"], "a", 2), 2)
    self.assertEqual(self.solution.closestTarget(["a", "b", "c", "d", "e"], "c", 3), 1)
    self.assertEqual(self.solution.closestTarget(["a", "b", "c", "d", "e"], "z", 0), -1)

if __name__ == "__main__":
  unittest.main()
