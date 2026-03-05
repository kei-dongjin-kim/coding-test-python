class Solution:
    def minOperations(self, s: str) -> int:
        l = len(s)
        case1, case2 = 0, 0
        for i in range(l):
            if i % 2 == 0:
                if s[i] == '0':
                    case1 += 1
                else:
                    case2 += 1
            else:
                if s[i] == '0':
                    case2 += 1
                else:
                    case1 += 1
        return min(case1, case2)