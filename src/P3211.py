from typing import List

class Solution:
    def validStrings(self, n: int) -> List[str]:
        
        init_val = ['0', '1']
        def backtrack(nn: int, li: list):
            if nn >= n:
                return li
            arr = []
            for s in li:
                if s[-1] == '1':
                    arr.append(s + '0')
                arr.append(s + '1')
            return backtrack(nn + 1, arr)
        
        return backtrack(1, init_val)
        