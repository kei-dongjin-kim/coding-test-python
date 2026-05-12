from typing import Optional
from UserDefinedDataType import TreeNode

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def helper(root: Optional[TreeNode], val):
            val = val * 2 + root.val
            if root.left is None and root.right is None:
                return val
            res = 0
            if root.left is not None:
                res += helper(root.left, val)
            if root.right is not None:
                res += helper(root.right, val)
            return res

        return helper(root, 0)
