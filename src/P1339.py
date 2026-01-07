from typing import Optional
from UserDefinedDataType import TreeNode

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        total = self.tree_sum(root)
        ans = self.helper(root, total)
        return ans % (10 ** 9 + 7)
    
    def helper(self, root: Optional[TreeNode], total: int) -> int:
        if root is None:
            return 0
        left = self.helper(root.left, total)
        right = self.helper(root.right, total)
        curr = (total - root.val) * root.val
        return max(left, right, curr)

    def tree_sum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = self.tree_sum(root.left)
        right = self.tree_sum(root.right)
        root.val += left + right
        return root.val
