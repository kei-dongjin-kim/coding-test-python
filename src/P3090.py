from collections import defaultdict

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        max_len = 0
        l = len(s)
        for left in range(l - 1):
            dict1 = defaultdict(int)
            for right in range(left, l):
                if dict1[s[right]] == 2:
                    break
                dict1[s[right]] += 1
                max_len = max(max_len, right - left + 1)
        return max_len
