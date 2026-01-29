class Solution:
    def isFascinating(self, n: int) -> bool:
        if n >= 500:
            return False
        thing1 = str(n) + str(n * 2) + str(n * 3)
        set1 = set()
        for c in thing1:
            if c in set1:
                return False
            elif c == '0':
                return False
            else:
                set1.add(c)
        return True