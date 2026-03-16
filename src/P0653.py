from UserDefinedDataType import TreeNode
from collections import deque
from typing import Optional

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        q = deque([root])
        while q:
            node = q.popleft()
            if k != node.val * 2: # not equal
                flag = self.search(root, k - node.val)
                if flag:
                    return True
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return False
    
    def search(self, node: Optional[TreeNode], k: int) -> Optional[TreeNode]:
        if node is None or node.val == k:
            return node
        if k < node.val:
            return self.search(node.left, k)
        return self.search(node.right, k)
