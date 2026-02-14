from typing import List

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        l = len(nums)
        # length 2
        if l == 2:
            return True
        # length 3
        if l == 3:
            if nums[0] >= nums[1] and nums[1] >= nums[2]:
                return False
            return True
        # length 4~
        cnt = 0
        if nums[0] >= nums[1]:
            cnt += 1
        for i in range(1, l - 2):
            if nums[i] >= nums[i + 1]:
                cnt += 1
                if nums[i] >= nums[i + 2] and nums[i - 1] >= nums[i + 1]:
                    return False
        if nums[l - 2] >= nums[l - 1]:
            cnt += 1
        if cnt > 1:
            return False
        return True