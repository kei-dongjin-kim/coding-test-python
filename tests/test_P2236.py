import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P2236 import TreeNode
from P2236 import Solution

class TestP2236(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    left = TreeNode(1)
    right = TreeNode(9)
    treeNode1 = TreeNode(10, left, right)
    self.assertTrue(self.solution.checkTree(treeNode1))

if __name__ == "__main__":
  unittest.main()