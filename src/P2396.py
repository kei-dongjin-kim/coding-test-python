class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for b in range(2, n - 1):
            nn = n
            base = ""
            while nn > 0:
                rest = nn % b
                base += str(rest)
                nn //= b
            if base != base[::-1]:
                return False
        return True