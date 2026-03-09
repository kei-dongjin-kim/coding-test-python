from typing import List
from collections import Counter
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        l = len(arr)
        dic = Counter(arr)
        keySorted = sorted(dic)
        left = l // 20
        right = left
        for k in keySorted:
            if dic[k] >= left:
                dic[k] -= left
                left = 0
                break
            else:
                left -= dic[k]
                dic[k] = 0
        for k in keySorted[::-1]:
            if dic[k] >= right:
                dic[k] -= right
                right = 0
                break
            else:
                right -= dic[k]
                dic[k] = 0
        my_sum = 0
        my_cnt = 0
        for k, v in dic.items():
            my_sum += k * v
            my_cnt += v
        return my_sum / my_cnt

# class Solution:
#     def trimMean(self, arr: List[int]) -> float:
#         arr.sort()
#         sum1, cnt1 = 0, 0
#         l = len(arr)
#         left = int(l * 0.05)
#         right = l - left
#         for i in range(left, right):
#             sum1 += arr[i]
#             cnt1 += 1
#         return sum1 / cnt1