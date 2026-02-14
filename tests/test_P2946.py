import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P2946 import Solution

class Testing(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.areSimilar([[1,2,3],[4,5,6],[7,8,9]], 2), False)

  def test2(self):
    self.assertEqual(self.solution.areSimilar([[1,2,3],[4,5,6],[7,8,9]], 3), True)

  def test3(self):
    self.assertEqual(self.solution.areSimilar([[1,1,1],[1,1,1],[1,1,1]], 2), True)

if __name__ == "__main__":
  unittest.main()