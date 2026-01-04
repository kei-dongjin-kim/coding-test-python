from typing import List

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_idx: int = 0
        max_val: int = 0
        for i, row in enumerate(mat):
            if (n := row.count(1)) > max_val:
                max_val = n
                max_idx = i
        return [max_idx, max_val]