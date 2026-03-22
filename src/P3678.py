from typing import List

class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        avg1 = sum(nums) / len(nums)
        curr = int(avg1) + 1
        if curr <= 0:
            curr = 1
        while curr in nums:
            curr += 1
        return curr
