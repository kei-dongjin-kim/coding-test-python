from typing import List

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = len(nums)
        for i in range(l):
            if nums[i] < 0 and k > 0:
                nums[i] *= -1
                k -= 1
            else:
                break
        if k % 2 == 1:
            nums.sort()
            nums[0] *= -1
        return sum(nums)