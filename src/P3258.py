class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        cnt = 0
        right = len(s)
        for left in range(right):
            c0, c1 = 0, 0
            for i in range(left, right):
                if s[i] == '0':
                    c0 += 1
                else:
                    c1 += 1
                if c0 <= k or c1 <= k:
                    cnt += 1
        return cnt