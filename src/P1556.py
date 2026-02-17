class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n == 0:
            return "0"
        ans = ""
        i = 0
        while n > 0:
            rest = n % 10
            if i != 0 and i % 3 == 0:
                ans = "." + ans
            ans = str(rest) + ans
            n //= 10
            i += 1
        return ans
