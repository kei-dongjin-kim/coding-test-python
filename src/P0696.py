class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        l = len(s)
        count = 0
        prev = s[0]
        for i in range(1, l):
            if prev != s[i]:
                left = i - 1
                right = i
                while 0 <= left and right < l and prev == s[left] and s[i] == s[right]:
                    count += 1
                    left -= 1
                    right += 1
            prev = s[i]
        return count