from collections import Counter

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        for key, val in freq1.items():
            if key in freq2:
                if abs(val - freq2[key]) > 3:
                    return False
                else:
                    freq2.pop(key)
            else:
                if val > 3:
                    return False
        for val in freq2.values():
            if val > 3:
                return False

        return True