class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        strn = str(n)
        strx = str(x)
        return strx in strn and strx != strn[:1]
