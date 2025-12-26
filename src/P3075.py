from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        n = len(happiness)
        d = 0
        ans = 0
        for i in range(k):
            ans += max(happiness[i] - d, 0)
            d += 1
        return ans