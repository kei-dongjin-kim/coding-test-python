class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        curr = n % 2
        n //= 2
        while n > 0:
            rest = n % 2
            if curr == rest:
                return False
            else:
                curr = rest
            n //= 2
        return True