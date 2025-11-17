from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        left = 0
        right = len(nums)
        for i in range(len(nums)):
            if nums[i] == 1:
                left = i
                break
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 1:
                right = i
                break
        
        count = 0
        for n in nums[left + 1:right + 1]:
            if n == 0:
                count += 1
            else:
                if count < k:
                    return False
                count = 0

        return True