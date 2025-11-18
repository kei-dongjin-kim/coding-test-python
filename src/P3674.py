from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                return 1
        return 0
