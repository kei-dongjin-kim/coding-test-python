from typing import List

class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        max1 = 0
        n = len(nums)
        for i in range(n):
            if (nums[i] % 2 == 0):
                curr1 = 0
                for j in range(n - i):
                    if (
                        nums[i + j] % 2 == j % 2 and
                        nums[i + j] <= threshold
                    ):
                        curr1 += 1
                    else:
                        break
                max1 = max(max1, curr1)

        return max1