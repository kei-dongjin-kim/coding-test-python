import unittest
import sys
import os

current_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(current_dir, "..", "src"))
sys.path.append(src_dir)

from P0637 import Solution
from UserDefinedDataType import TreeNode

class Testing(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    root: TreeNode = TreeNode(10)
    root.left = TreeNode(10)
    root.right = TreeNode(10)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(10)
    self.assertEqual(self.solution.averageOfLevels(root), [10.00000, 10.00000, 10.00000])

if __name__ == "__main__":
  unittest.main()