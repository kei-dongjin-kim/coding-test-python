class Solution:
    def isThree(self, n: int) -> bool:
        if n < 4:
            return False
        sq = n ** 0.5
        if sq % 1 != 0:
            return False
        for a in range(2, int(sq)):
            di = n // a
            if di * a == n:
                return False
        return True