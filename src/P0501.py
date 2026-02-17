from collections import defaultdict
from typing import List, Optional

from UserDefinedDataType import TreeNode

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        di: dict = defaultdict(int)
        def counting(root: Optional[TreeNode]) -> None:
            if root is None:
                return
            di[root.val] += 1
            counting(root.left)
            counting(root.right)
        
        counting(root)
        max_val = max(di.values())
        return [key for key, val in di.items() if val == max_val]

