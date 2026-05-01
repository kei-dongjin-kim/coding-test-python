from typing import List

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            if i == s:
                return i
        return -1