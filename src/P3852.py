from collections import Counter

class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        freq = Counter(nums)
        keys = sorted(freq)

        if len(keys) < 2:
            return [-1, -1]

        first = keys[0]
        first_freq = freq[first]

        for k in keys[1:]:
            if first_freq != freq[k]:
                return [first, k]

        return [-1, -1]
