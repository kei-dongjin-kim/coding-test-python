from typing import List

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        arr: List[str] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        res: str = ""
        if num < 0:
            num += 2 ** 32
        while num > 0:
            rest: int = num % 16
            res = arr[rest] + res
            num //= 16
        return res