import unittest
import sys
import os

current_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(current_dir, "..", "src"))
sys.path.append(src_dir)

from P0617 import Solution
from UserDefinedDataType import TreeNode

class TestP0617(unittest.TestCase):
  def setUp(self):
    self.solution = Solution()

  def test1(self):
    root1: TreeNode = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
    root2: TreeNode = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
    actual: TreeNode = self.solution.mergeTrees(root1, root2)
    expected: TreeNode = TreeNode(2, TreeNode(4, TreeNode(8), TreeNode(10)), TreeNode(6, TreeNode(12), TreeNode(14)))
    self.assertEqual(actual, expected)

if __name__ == "__main__":
  unittest.main()