class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        vowels = 'aeiou'
        l = len(s)
        for i in range(l - 1, -1, -1):
            if s[i] not in vowels:
                return s[:i + 1]
        return ''