from typing import List

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_len = 0
        min_arr = []
        for [l, w] in rectangles:
            min_val = min(l, w)
            min_arr.append(min_val)
            max_len = max(max_len, min_val)
        return min_arr.count(max_len)