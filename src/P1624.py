class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        max_val = -1
        dict1 = {}
        l = len(s)
        for i in range(l):
            if s[i] in dict1:
                max_val = max(max_val, i - dict1[s[i]] - 1)
            else:
                dict1[s[i]] = i
        return max_val
