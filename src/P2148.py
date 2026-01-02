from typing import List

class Solution:
    def countElements(self, nums: List[int]) -> int:
        min1 = nums[0]
        max1 = nums[0]
        for n in nums:
            min1 = min(min1, n)
            max1 = max(max1, n)
        cnt = 0
        for n in nums:
            if min1 < n and n < max1:
                cnt += 1
        return cnt
