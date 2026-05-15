from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        set1 = set()
        for arr in nums:
            [start, end] = arr
            for n in range(start, end + 1):
                set1.add(n)
        return len(set1)