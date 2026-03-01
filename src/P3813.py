from math import floor

class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowels = "aeiou"
        v = 0
        c = 0
        for a in s:
            if a.isalpha():
                if a in vowels:
                    v += 1
                else:
                    c += 1
        if c == 0:
            return 0
        return floor(v / c)