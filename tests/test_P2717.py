import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P2717 import Solution

class Testing(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
  
    def test1(self):
        self.assertEqual(self.solution.semiOrderedPermutation([2, 3, 1, 5, 4]), 3)

    def test2(self):
        self.assertEqual(self.solution.semiOrderedPermutation([1, 3, 4, 2, 5]), 0)

    def test3(self):
        self.assertEqual(self.solution.semiOrderedPermutation([2, 3, 5, 1, 4]), 4)

if __name__ == "__main__":
    unittest.main()
