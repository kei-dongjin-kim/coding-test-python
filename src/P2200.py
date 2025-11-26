from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = []
        curr = 0
        length = len(nums)
        for i in range(length):
            if (nums[i] == key):
                left = max(curr, i - k)
                right = min(length, i + k + 1)
                for j in range(left, right):
                    res.append(j)
                    curr = j + 1
        return res