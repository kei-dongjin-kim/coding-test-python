from typing import List

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        max_diff = 0
        for i in range(1, n):
            max_diff = max(max_diff, abs(nums[i] - nums[i - 1]))
        max_diff = max(max_diff, abs(nums[n - 1] - nums[0]))
        return max_diff