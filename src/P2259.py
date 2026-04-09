class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        l = len(number)
        max_val = 0
        for i in range(l):
            if number[i] == digit:
                curr = int(number[:i] + number[i+1:])
                max_val = max(max_val, curr)
        return str(max_val)