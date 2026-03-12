class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        result = 0
        p = 0
        while n > 0:
            rest = n % 2
            rev = 0 if rest == 1 else 1
            result += rev * (2 ** p)
            n //= 2
            p += 1
        return result