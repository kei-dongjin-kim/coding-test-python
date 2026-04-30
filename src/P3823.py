class Solution:
    def reverseByType(self, s: str) -> str:
        a = []
        b = []
        res = ""
        for c in s:
            if c.isalpha():
                a.append(c)
            else:
                b.append(c)
        for c in s:
            if c.isalpha():
                res += a.pop()
            else:
                res += b.pop()
        return res
