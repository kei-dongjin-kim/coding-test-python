from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        nums.sort()
        mn = nums[-1]
        for i in range(k - 1, n):
            mn = min(mn, nums[i] - nums[i - (k - 1)])
        return mn