import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P1339 import Solution
from UserDefinedDataType import TreeNode

class TestP1339(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    node4: TreeNode = TreeNode(4)
    node5: TreeNode = TreeNode(5)
    node6: TreeNode = TreeNode(6)
    node7: TreeNode = TreeNode(7)
    node2: TreeNode = TreeNode(2, node4, node5)
    node3: TreeNode = TreeNode(3, node6, node7)
    root: TreeNode = TreeNode(1, node2, node3)
    self.assertEqual(self.solution.maxProduct(root), 192)

if __name__ == "__name__":
  unittest.main()
