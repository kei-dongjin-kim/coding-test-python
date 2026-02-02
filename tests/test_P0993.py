import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P0993 import Solution
from UserDefinedDataType import TreeNode

class TestP0993(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.isCousins(
      root=TreeNode(
        1,
        left=TreeNode(
          2,
          left=TreeNode(4),
          right=TreeNode(5)
        ),
        right=TreeNode(
          3,
          left=TreeNode(6),
          right=TreeNode(7)
        )
      ),
      x=5,
      y=7
    ), True)

if __name__ == "__main__":
  unittest.main()
