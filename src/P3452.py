from typing import List

class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        l = len(nums)
        res = 0
        for i in range(l):
            left = False
            right = False
            li = i - k
            ri = i + k
            if li < 0:
                left = True
            elif nums[li] < nums[i]:
                left = True
            if l - 1 < ri:
                right = True
            elif nums[ri]  < nums[i]:
                right = True
            if left and right:
                res += nums[i]
        return res