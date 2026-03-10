class Solution:
    def smallestNumber(self, n: int) -> int:
        res = 0
        p = 0
        while n > 0:
            n //= 2
            res += 2 ** p
            p += 1
        return res

        # bin_str = f'{n:b}'.replace('0', '1')
        # return int(bin_str, 2)
