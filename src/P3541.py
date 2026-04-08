from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        max_vowel = 0
        max_consonant = 0
        vowels = 'aeiou'
        cc = Counter(s)
        for key, val in cc.items():
            if key in vowels:
                max_vowel = max(max_vowel, val)
            else:
                max_consonant = max(max_consonant, val)
        return max_vowel + max_consonant
