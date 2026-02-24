from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        set1 = set(nums)
        list1 = [n for n in set1]
        list1.sort()
        if list1[-1] <= 0:
            return list1[-1]
        sum1 = 0
        for n in set1:
            if n > 0:
                sum1 += n
        return sum1