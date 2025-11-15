import string

class Solution:
    def concatHex36(self, n: int) -> str:
        digits36 = string.digits + string.ascii_uppercase

        p2 = n ** 2
        p2res = ""
        while p2 >= 16:
            p2res += digits36[p2 % 16]
            p2 //= 16
        if p2 > 0:
            p2res += digits36[p2]
        
        p3 = n ** 3
        p3res = ""
        while p3 >= 36:
            p3res += digits36[p3 % 36]
            p3 //= 36
        if p3 > 0:
            p3res += digits36[p3]

        return p2res[::-1] + p3res[::-1]