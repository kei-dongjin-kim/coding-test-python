
from typing import Optional
from UserDefinedDataType import TreeNode

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.min_val = float('inf')
        def helper(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            helper(node.left)
            if self.prev is not None:
                self.min_val = min(self.min_val, node.val - self.prev)
            self.prev = node.val
            helper(node.right)
        helper(root)
        return self.min_val
