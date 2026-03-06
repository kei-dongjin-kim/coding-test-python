from typing import List

class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        set_nums = set(nums)
        sorted_nums = sorted(set_nums, reverse=True)
        return sorted_nums[:k]