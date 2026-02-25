from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        min_val = 1000
        l = len(nums)
        for i in range(l - 2):
            for j in range(i + 1, l - 1):
                if nums[i] == nums[j]:
                    for k in range(j + 1, l):
                        if nums[j] == nums[k]:
                            curr_val = abs(i - j) + abs(j - k) + abs(k - i)
                            min_val = min(min_val, curr_val)
        return -1 if min_val == 1000 else min_val