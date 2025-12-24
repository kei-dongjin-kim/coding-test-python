import re
from typing import List

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        n = len(code)
        confirmed = []
        bList = ["electronics", "grocery", "pharmacy", "restaurant"]
        for i in range(n):
            if (
                self.is_valid_string(code[i]) and 
                businessLine[i] in bList and 
                isActive[i]
            ):
                confirmed.append(Coupon(code[i], businessLine[i]))
        
        sorted1 = sorted(confirmed, key=lambda p: p.code)
        sorted2 = sorted(sorted1, key=lambda p: p.businessLine)
        res = [coupon.code for coupon in sorted2]
        return res

    def is_valid_string(self, s: str) -> bool:
        pattern = r'^\w+$'
        return bool(re.match(pattern, s))

class Coupon:
    def __init__(self, code, businessLine):
        self.code = code
        self.businessLine = businessLine
