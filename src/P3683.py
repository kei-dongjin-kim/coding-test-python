from typing import List

class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        min_val = float('inf')
        for t in tasks:
            min_val = min(min_val, t[0] + t[1])
        return min_val