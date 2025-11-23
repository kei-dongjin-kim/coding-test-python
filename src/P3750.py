class Solution:
    def minimumFlips(self, n: int) -> int:
        binStr = format(n, "b")
        revStr = binStr[::-1]
        count = 0
        for i in range(len(binStr)):
            if binStr[i] != revStr[i]:
                count += 1
        return count