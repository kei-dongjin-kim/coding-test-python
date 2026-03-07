from typing import List

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        cnt = 0
        left = 0
        right = sum(nums)
        for n in nums:
            left += n
            right -= n
            if n == 0:
                if left == right:
                    cnt += 2
                elif abs(left - right) == 1:
                    cnt += 1
        return cnt
        