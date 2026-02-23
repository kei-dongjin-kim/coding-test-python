class Solution:
    def secondHighest(self, s: str) -> int:
        first = -1
        second = -1
        for c in s:
            if c.isdigit():
                curr = int(c)
                if first < curr:
                    second = first
                    first = curr
                elif second < curr and curr < first:
                    second = curr
        return second