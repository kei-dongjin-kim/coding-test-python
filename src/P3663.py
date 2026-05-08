from collections import Counter

class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        freq = Counter(str(n))
        min_key = -1
        min_val = float('inf')
        for s_key, val in freq.items():
            key = int(s_key)
            if min_key == -1:
                min_key = key
                min_val = val
            else:
                if val < min_val:
                    min_key = key
                    min_val = val
                elif val == min_val:
                    if key < min_key:
                        min_key = key
                        min_val = val
        return min_key