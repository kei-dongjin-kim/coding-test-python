from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if nums[0] >= nums[1] or nums[n - 2] >= nums[n - 1]:
            return False
        left = 0
        right = n - 1
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                left = i
            else:
                break
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                right = i
            else:
                break
        if left >= right:
            return False
        for i in range(left, right):
            if nums[i] <= nums[i + 1]:
                return False
        return True
