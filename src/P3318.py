from typing import List
from collections import Counter

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans: List[int] = []
        freq = Counter(nums[:k])
        sorted_items = sorted(freq.items(), key=lambda x: (x[1], x[0]), reverse=True)
        xsum = 0
        for j in range(min(x, len(sorted_items))):
            xsum += sorted_items[j][0] * sorted_items[j][1]
        ans.append(xsum)
        for i in range(k, n):
            freq[nums[i]] += 1
            freq[nums[i - k]] -= 1
            sorted_items = sorted(freq.items(), key=lambda x: (x[1], x[0]), reverse=True)
            xsum = 0
            for j in range(min(x, len(sorted_items))):
                xsum += sorted_items[j][0] * sorted_items[j][1]
            ans.append(xsum)
        return ans