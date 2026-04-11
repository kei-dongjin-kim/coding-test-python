from collections import Counter
from typing import List

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        freq = Counter(deck).values()
        min_cnt = min(freq)
        if min_cnt == 1:
            return False
        for n in range(2, min_cnt + 1):
            flag = True
            for val in freq:
                if val % n != 0:
                    flag = False
                    break
            if flag:
                return True
        return False