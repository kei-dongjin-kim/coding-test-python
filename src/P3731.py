from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        result = []
        nums.sort()
        for i in range(1, len(nums)):
            prev = nums[i - 1]
            curr = nums[i]
            if prev + 1 != curr:
                for j in range(prev + 1, curr):
                    result.append(j)
        return result