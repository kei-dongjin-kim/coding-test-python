
from UserDefinedDataType import TreeNode
from typing import Optional

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return
        elif root1 is None:
            return root2
        elif root2 is None:
            return root1

        val = root1.val + root2.val
        left = self.mergeTrees(root1.left, root2.left)
        right = self.mergeTrees(root1.right, root2.right)
        return TreeNode(val, left, right)