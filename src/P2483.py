from typing import List

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        min_idx = 0
        min_val = float('inf')
        n = len(customers)

        temp_y: List[int] = [0]
        for s in customers[::-1]:
            curr = 1 if s == 'Y' else 0
            temp_y.append(temp_y[-1] + curr)
        prefix_y = temp_y[::-1]

        prefix_n: List[int] = [0]
        for s in customers:
            curr = 1 if s == 'N' else 0
            prefix_n.append(prefix_n[-1] + curr)

        for i in range(n + 1):
            curr = prefix_y[i] + prefix_n[i]
            if min_val > curr:
                min_val = curr
                min_idx = i

        return min_idx