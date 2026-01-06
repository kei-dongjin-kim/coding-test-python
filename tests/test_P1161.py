import unittest
import sys
import os

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P1161 import Solution
from UserDefinedDataType import TreeNode

class TestP1161(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.maxLevelSum(
      TreeNode(9,
        TreeNode(1,
          TreeNode(7),
          TreeNode(8)),
        TreeNode(2)
      )
    ), 3)

if __name__ == "__main__":
  unittest.main()
