from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        mx = 0
        left_pre = -1
        for i in range(n - 1):
            if left_pre == colors[i]:
                continue
            right_pre = -1
            for j in range(n - 1, i, -1):
                if right_pre == colors[j]:
                    continue
                if colors[i] != colors[j]:
                    mx = max(mx, j - i)
                    break
                right_pre = colors[j]
            left_pre = colors[i]
        return mx