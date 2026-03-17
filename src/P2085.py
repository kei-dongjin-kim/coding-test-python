from typing import List
from collections import Counter

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        cnt = 0
        dic1 = Counter(words1)
        dic2 = Counter(words2)
        for key, val in dic1.items():
            if val == 1 and dic2[key] == 1:
                cnt += 1
        return cnt