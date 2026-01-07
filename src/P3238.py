from collections import Counter
from typing import List

class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        cnt: int = 0
        di: dict = {}
        for p in pick:
            if p[0] in di:
                di[p[0]].append(p[1])
            else:
                di[p[0]] = [p[1]]
        for key, val in di.items():
            ma = Counter(val)
            for mk, mv in ma.items():
                if key < mv:
                    cnt += 1
                    break
        return cnt