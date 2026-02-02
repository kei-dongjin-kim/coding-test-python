from typing import Optional, Tuple
from UserDefinedDataType import TreeNode

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False

        x_info = self.find(root, x, parent=None, depth=0)
        y_info = self.find(root, y, parent=None, depth=0)

        if x_info is None or y_info is None:
            return False

        x_parent, x_depth = x_info
        y_parent, y_depth = y_info
        return x_parent != y_parent and x_depth == y_depth

    def find(
        self,
        root: Optional[TreeNode],
        target: int,
        parent: Optional[int],
        depth: int
    ) -> Optional[Tuple[Optional[int], int]]:
        if root is None:
            return None
        if root.val == target:
            return (parent, depth)

        left = self.find(root.left, target, root.val, depth + 1)
        if left is not None:
            return left
        return self.find(root.right, target, root.val, depth + 1)