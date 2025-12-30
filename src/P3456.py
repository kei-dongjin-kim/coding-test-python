class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        n = len(s)
        for i in range(k - 1, n):
            con1: bool = True
            for j in range(i - k + 1, i):
                con1 = s[j] == s[i]
                if con1 == False:
                    break
            con2: bool = True
            if i - k >= 0:
                if s[i] == s[i - k]:
                    con2 = False
            con3: bool = True
            if i + 1 < n:
                if s[i] == s[i + 1]:
                    con3 = False
            if con1 and con2 and con3:
                return True
        return False