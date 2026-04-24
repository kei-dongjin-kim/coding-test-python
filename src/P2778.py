from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        res = 0
        l = len(nums)
        for i in range(l):
            if l % (i + 1) == 0:
                res += nums[i] * nums[i]
        return res