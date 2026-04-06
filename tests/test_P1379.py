import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from UserDefinedDataType import TreeNode
from P1379 import Solution

class Testing(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    original = TreeNode(4)
    original.left = TreeNode(2)
    original.left.left = TreeNode(1)
    original.left.right = TreeNode(3)
    original.right = TreeNode(6)
    original.right.left = TreeNode(5)
    original.right.right = TreeNode(7)
    cloned = TreeNode(4)
    cloned.left = TreeNode(2)
    cloned.left.left = TreeNode(1)
    cloned.left.right = TreeNode(3)
    cloned.right = TreeNode(6)
    cloned.right.left = TreeNode(5)
    cloned.right.right = TreeNode(7)
    answer = TreeNode(6)
    answer.left = TreeNode(5)
    answer.right = TreeNode(7)
    self.assertEqual(self.solution.getTargetCopy(
      original,
      cloned,
      TreeNode(6)
    ), answer)

if __name__ == "__main__":
  unittest.main()
