class Solution:
    def minimumChairs(self, s: str) -> int:
        max_val = 0
        chair = 0
        for c in s:
            if c == 'E':
                chair += 1
                max_val = max(max_val, chair)
            else:
                chair -= 1
        return max_val