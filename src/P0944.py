from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cnt = 0
        row = len(strs)
        if row <= 1:
            return 0
        col = len(strs[0])
        for c in range(col):
            for r in range(1, row):
                if strs[r - 1][c] > strs[r][c]:
                    cnt += 1
                    break
        return cnt