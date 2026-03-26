from typing import List

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        curr = 0
        res = -1
        l = len(bits)
        while curr < l:
            if bits[curr] == 0:
                curr += 1
                res = 1
            else:
                curr += 2
                res = 2
        return res == 1