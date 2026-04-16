from typing import List

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        l = len(words)
        for i in range(l // 2 + 1):
            left = (startIndex - i) % l
            if words[left] == target:
                return i
            right = (startIndex + i) % l
            if words[right] == target:
                return i
        return -1