import unittest
import sys
import os

curr_dir = os.path.dirname(__name__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P0501 import Solution
from UserDefinedDataType import TreeNode

class Testing(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    root = TreeNode(1)
    root.right = TreeNode(5)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(9)
    root.right.right.left = TreeNode(9)
    self.assertEqual(self.solution.findMode(root), [5, 9])

if __name__ == "__main__":
  unittest.main()