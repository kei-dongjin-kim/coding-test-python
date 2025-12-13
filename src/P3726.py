class Solution:
    def removeZeros(self, n: int) -> int:
        res = 0
        pow = 0
        while n > 0:
            rest = n % 10
            if rest != 0:
                res += rest * (10 ** pow)
                pow += 1
            n //= 10
        return res