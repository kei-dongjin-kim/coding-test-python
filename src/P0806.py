from typing import List

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        dic = {}
        for i in range(len(widths)):
            dic[chr(i + 97)] = widths[i]
        
        count = 1
        sum = 0
        for c in s:
            if sum + dic[c] > 100:
                sum = dic[c]
                count += 1
            else:
                sum += dic[c]
        
        return [count, sum]