from typing import List

class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        dic = {}
        r = len(grid)
        c = len(grid[0])
        for i in range(r):
            sum = 0
            for j in range(c):
                sum += grid[i][j]
            dic[i] = sum

        max_key = -1
        max_val = -1
        for key, val in dic.items():
            if max_val < val:
                max_key = key
                max_val = val
        
        return max_key