import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P0653 import Solution
from UserDefinedDataType import TreeNode

class Testing(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    root = TreeNode(5, TreeNode(4), TreeNode(6))
    self.assertEqual(self.solution.findTarget(root, 10), True)

if __name__ == "__main__":
  unittest.main()
