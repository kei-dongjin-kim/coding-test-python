from typing import List

class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        val = 0
        l = len(nums)
        for i in range(k):
            val += nums[l - 1 - i]
            val -= nums[i]
        return val