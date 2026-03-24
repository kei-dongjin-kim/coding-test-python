from typing import List

class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        def encrypt(x: int) -> int:
            res = 0
            max_val = 0
            unit = 0
            while x > 0:
                rest = x % 10
                max_val = max(max_val, rest)
                x //= 10
                unit += 1
            for p in range(unit):
                res += max_val * (10 ** p)
            return res

        ans = 0
        for n in nums:
            ans += encrypt(n)
        return ans
