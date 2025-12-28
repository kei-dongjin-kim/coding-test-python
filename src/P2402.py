from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        list_end: List[int] = [0] * n
        list_cnt: List[int] = [0] * n
        meetings.sort(key=lambda x: x[0])

        for m in meetings:
            flag = True
            for i in range(n):
                if list_end[i] <= m[0]:
                    list_end[i] = m[1]
                    list_cnt[i] += 1
                    flag = False
                    break
            
            if flag:
                min_idx = 0
                min_val = list_end[0]
                for i in range(1, n):
                    if min_val > list_end[i]:
                        min_val = list_end[i]
                        min_idx = i

                list_end[min_idx] += m[1] - m[0]
                list_cnt[min_idx] += 1

        max_idx = 0
        max_val = list_cnt[0]
        for i in range(1, n):
            if max_val < list_cnt[i]:
                max_val = list_cnt[i]
                max_idx = i

        return max_idx