from collections import Counter

class Solution:
    def findValidPair(self, s: str) -> str:
        map1 = Counter(s)
        list1 = []
        for key, val in map1.items():
            if key == str(val):
                list1.append(key)
        for i in range(1, len(s)):
            if s[i - 1] != s[i] and s[i - 1] in list1 and s[i] in list1:
                return s[i - 1: i + 1]
        return ""