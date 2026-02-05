from typing import List

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num_int = 0
        for n in num:
            num_int += n
            num_int *= 10
        num_int //= 10
        num_int += k
        ls: int = []
        while num_int > 0:
            rest = num_int % 10
            ls.append(rest)
            num_int //= 10
        return ls[::-1]