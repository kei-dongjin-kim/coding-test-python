from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        l = len(nums)
        inc = 0
        cur = nums[0]
        for i in range(1, l):
            if cur < nums[i]:
                cur = nums[i]
            else:
                inc += cur - nums[i] + 1
                cur += 1
        return inc