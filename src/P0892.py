from typing import List

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        total = 0
        n = len(grid)
        for r in range(n):
            for c in range(n):
                if grid[r][c] > 0:
                    total += grid[r][c] * 4 + 2
                if r > 0:
                    total -= 2 * min(grid[r][c], grid[r - 1][c])
                if c > 0:
                    total -= 2 * min(grid[r][c], grid[r][c - 1])
        return total