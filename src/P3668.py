from typing import List

class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        f_set = set(friends)
        return [o for o in order if o in f_set]
