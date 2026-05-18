from typing import List

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0:
            return False
        p = total // 3
        if p == 0:
            count = 0
            subsum = 0
            for a in arr:
                subsum += a
                if subsum == 0:
                    count += 1
            return count >= 3
        count = 0
        subsum = 0
        for a in arr:
            subsum += a
            if count < 2 and subsum == p:
                subsum = 0
                count += 1
        return count == 2 and subsum == p