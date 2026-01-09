from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mi = (left + right) // 2
            if target == nums[mi]:
                return mi
            elif target > nums[mi]:
                left = mi + 1
            else:
                right = mi - 1
        return left