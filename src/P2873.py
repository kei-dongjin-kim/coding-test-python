from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_val = 0
        l = len(nums)
        for i in range(l - 2):
            for j in range(i + 1, l - 1):
                for k in range(j + 1, l):
                    curr = (nums[i] - nums[j]) * nums[k]
                    max_val = max(max_val, curr)
        return max_val