class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        cnt = 0
        for n in range(low, high + 1):
            dgt = []
            while n > 0:
                rest = n % 10
                dgt.append(rest)
                n //= 10
            l = len(dgt)
            if l % 2 == 0:
                mid = 0
                left = 0
                right = l - 1
                while left < right:
                    mid += dgt[left] - dgt[right]
                    left += 1
                    right -= 1
                if mid == 0:
                    cnt += 1
        return cnt