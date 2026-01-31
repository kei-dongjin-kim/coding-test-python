from typing import List

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        mn = min(nums)
        mx = max(nums)
        out = mx - mn - (k * 2)
        if out > 0:
            return out
        return 0