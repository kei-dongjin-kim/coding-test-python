from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cnt: int = 0
        rc = len(grid)
        cc = len(grid[0])
        for r in range(rc):
            if grid[r][0] < 0:
                cnt += (rc - r) * cc
                break
            for c in range(cc):
                if grid[r][c] < 0:
                    cnt += cc - c
                    break
        return cnt