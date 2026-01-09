from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max1 = 0
        n = len(height)
        left = 0
        right = n - 1
        while left < right:
            min_axis = min(height[left], height[right])
            width = right - left
            max1 = max(max1, min_axis * width)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max1