from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        sec: int = 0
        for i in range(1, len(points)):
            gap_x = abs(points[i][0] - points[i - 1][0])
            gap_y = abs(points[i][1] - points[i - 1][1])
            sec += max(gap_x, gap_y)
        return sec