class Solution:
    def maxDistinct(self, s: str) -> int:
        set1 = set()
        for c in s:
            set1.add(c)
        return len(set1)