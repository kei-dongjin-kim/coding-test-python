from collections import deque
from typing import List, Optional
from UserDefinedDataType import TreeNode

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        ans = []
        while queue:
            sum, cnt = 0, 0
            l = len(queue)
            for i in range(l):
                curr = queue.popleft()
                if curr is None or curr.val is None:
                    continue
                sum += curr.val
                cnt += 1
                queue.append(curr.left)
                queue.append(curr.right)
            if cnt:
                ans.append(float(sum / cnt))
        return ans
