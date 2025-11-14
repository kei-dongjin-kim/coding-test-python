from typing import List

class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        count = 0
        for p in batteryPercentages:
            if p - count > 0:
                count += 1
        
        return count