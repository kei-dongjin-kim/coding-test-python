class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0

        count = 0
        dic = {}

        for c in s[:3]:
            dic[c] = dic.get(c, 0) + 1

        if self.checkGood(dic):
            count += 1

        for i in range(3, len(s)):
            dic[s[i]] = dic.get(s[i], 0) + 1

            left = s[i - 3]
            dic[left] -= 1
            if dic[left] == 0:
                del dic[left]

            if self.checkGood(dic):
                count += 1

        return count
    
    def checkGood(self, d: dict) -> bool:
        if len(d) != 3:
            return False

        for value in d.values():
            if value != 1:
                return False

        return True
        