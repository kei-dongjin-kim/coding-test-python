from typing import List

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = ""
        for w in words:
            weight = 0
            for c in w:
                weight += weights[ord(c) - ord('a')]
            weight %= 26
            res += chr(ord('z') - weight)
        return res