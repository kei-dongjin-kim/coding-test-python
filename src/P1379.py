from UserDefinedDataType import TreeNode

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original is None:
            return

        if original.val == target.val:
            return cloned

        left = self.getTargetCopy(
            original.left,
            cloned.left,
            target
        )
        if left is not None:
            return left

        right = self.getTargetCopy(
            original.right,
            cloned.right,
            target
        )
        if right is not None:
            return right