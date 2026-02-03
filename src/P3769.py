from typing import List

class Pair:
    def __init__(self, origin: int, ref: int):
        self.origin = origin
        self.ref = ref

class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        ls: List[Pair] = []
        for origin in nums:
            binary_string = format(origin, 'b')
            reflected_string = binary_string[::-1]
            ref = int(reflected_string, 2)
            ls.append(Pair(origin, ref))
        return [x.origin for x in sorted(ls, key=lambda x: (x.ref, x.origin))]