from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        l = len(nums)
        idx_1 = nums.index(1)
        idx_n = nums.index(l)
        not_overlapped = idx_1 + (l - idx_n - 1)

        if idx_1 < idx_n:
            return not_overlapped
        
        return not_overlapped - 1
