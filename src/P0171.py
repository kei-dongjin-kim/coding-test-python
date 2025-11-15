class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        comp = 0

        for c in reversed(columnTitle):
            res += (26 ** comp) * (ord(c) - ord('A') + 1)
            comp += 1

        return res