from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        odd_max = float('-inf')
        even_min = float('inf')

        for val in freq.values():
            if val % 2 == 0:
                even_min = min(even_min, val)
            else:
                odd_max = max(odd_max, val)

        return odd_max - even_min