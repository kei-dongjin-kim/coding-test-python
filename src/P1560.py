from typing import List

class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        start = rounds[0]
        end = rounds[-1]
        
        if start <= end:
            return sorted(list(range(start, end + 1)))
        
        return sorted(list(range(start, n + 1)) + list(range(1, end + 1)))
