import unittest
import sys
import os

curr_dir = os.path.dirname(__name__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from UserDefinedDataType import TreeNode
from P0530 import Solution

class Testing(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(3)
    self.assertEqual(self.solution.getMinimumDifference(root), 1)

if __name__ == "__main__":
  unittest.main()