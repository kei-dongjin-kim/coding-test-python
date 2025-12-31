from typing import List
from collections import deque

class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen = deque()
        ans = []
        previous = 0
        k = 0
        for n in nums:
            if n == -1:
                if previous == -1:
                    k += 1
                else:
                    k = 1
                if len(seen) >= k:
                    ans.append(seen[k - 1])
                else:
                    ans.append(-1)
            else:
                seen.appendleft(n)
                k = 0
            previous = n
        return ans