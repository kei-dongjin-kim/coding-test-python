class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        c0 = 0
        c1 = 0
        mx = 0
        previous = ""
        for c in s:
            if previous == "0":
                if c == "0":
                    c0 += 1
                else:
                    c1 = 1
                    mx = max(mx, min(c0, c1))
            elif previous == "1":
                if c == "0":
                    c0 = 1
                else:
                    c1 += 1
                    mx = max(mx, min(c0, c1))
            else:
                if c == "0":
                    c0 += 1
                else:
                    c1 += 1
            previous = c
        return mx * 2