class Solution:
    def minTimeToType(self, word: str) -> int:
        cnt = 0
        pointer = 'a'
        for c in word:
            gap = abs(ord(c) - ord(pointer))
            cnt += min(gap, 26 - gap) + 1
            pointer = c
        return cnt