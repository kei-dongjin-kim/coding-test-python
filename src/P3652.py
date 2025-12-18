from typing import List

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        h = k // 2
        max_val = 0
        curr_val = 0
        for i in range(n):
            max_val += prices[i] * strategy[i]
        for i in range(h, k):
            curr_val += prices[i]
        for i in range(k, n):
            curr_val += prices[i] * strategy[i]
        max_val = max(max_val, curr_val)
        for i in range(1, n - k + 1):
            curr_val += prices[i - 1] * strategy[i - 1]
            curr_val -= prices[i + h - 1]
            curr_val += prices[i + k - 1] - (prices[i + k - 1] * strategy[i + k - 1])
            max_val = max(max_val, curr_val)
        return max_val