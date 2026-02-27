from typing import List

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        sum1, cnt1 = 0, 0
        l = len(arr)
        left = int(l * 0.05)
        right = l - left
        for i in range(left, right):
            sum1 += arr[i]
            cnt1 += 1
        return sum1 / cnt1