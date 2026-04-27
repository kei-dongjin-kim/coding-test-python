class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        min_val = float('inf')
        min_idx = -1
        for i in range(len(capacity)):
            if capacity[i] >= itemSize:
                if min_val > capacity[i]:
                    min_val = capacity[i]
                    min_idx = i
        return min_idx