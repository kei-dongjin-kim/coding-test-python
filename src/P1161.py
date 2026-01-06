from typing import Optional
from UserDefinedDataType import TreeNode

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        di: dict = {}
        out = self.helper(root, di, 1)
        max_val = float('-inf')
        max_key = 1
        for key, val in out.items():
            if val > max_val:
                max_val = val
                max_key = key
        return max_key


    def helper(self, root: Optional[TreeNode], di: dict, lvl: int) -> dict:
        if root is None:
            return di
        
        if lvl in di:
            di[lvl] += root.val
        else:
            di[lvl] = root.val

        self.helper(root.left, di, lvl + 1)
        self.helper(root.right, di, lvl + 1)

        return di