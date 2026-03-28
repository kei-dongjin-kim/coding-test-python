from typing import List

class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        res = []
        tm = len(grid)
        tn = len(grid[0])
        for n in range(tn):
            max_len = 0
            for m in range(tm):
                cur_len = len(str(grid[m][n]))
                max_len = max(max_len, cur_len)
            res.append(max_len)
        return res