from typing import List
import math

class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        max_val: int = 0
        l = len(nums)
        for ri in range(l):
            for ci in range(l):
                if ri == ci or l - ri - 1 == ci:
                    if self.is_prime(nums[ri][ci]):
                        max_val = max(max_val, nums[ri][ci])
        return max_val


    def is_prime(self, num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True