from typing import List
from collections import Counter

class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        di = Counter(nums)
        su = 0
        for key, val in di.items():
            if val % k == 0:
                su += key * val
        return su