from typing import List

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        n = len(capacity)
        sum1 = 0
        for a in apple:
            sum1 += a
        capacity.sort(reverse=True)
        for i in range(n):
            sum1 -= capacity[i]
            if sum1 <= 0:
                return i + 1
        return n