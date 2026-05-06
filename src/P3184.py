from typing import List

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        cnt = 0
        l = len(hours)
        for i in range(l - 1):
            for j in range(i + 1, l):
                if (hours[i] + hours[j]) % 24 == 0:
                    cnt += 1
        return cnt