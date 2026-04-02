from typing import List
from collections import Counter

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        di = Counter(nums)
        for val in di.values():
            if val % 2 != 0:
                return False
        return True