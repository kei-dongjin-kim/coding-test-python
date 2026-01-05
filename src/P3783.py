class Solution:
    def mirrorDistance(self, n: int) -> int:
        copied: int = n
        rev: int = 0
        while copied > 0:
            rest: int = copied % 10
            rev = rev * 10 + rest
            copied //= 10
        return abs(n - rev)