from typing import List
from collections import Counter

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        di = Counter(nums)
        if k == 1:
            max1 = -1
            for k, v in di.items():
                if v == 1:
                    max1 = max(max1, k)
            return max1
        if len(nums) == k:
            max1 = -1
            for k in di.keys():
                max1 = max(max1, k)
            return max1
        largest1 = max(nums[0], nums[-1])
        if di[largest1] == 1:
            return largest1 
        largest2 = min(nums[0], nums[-1])
        if di[largest2] == 1:
            return largest2
        return -1