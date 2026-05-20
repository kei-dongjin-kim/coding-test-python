from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        curr = 0
        l = len(A)
        arr = [False] * (l + 1)
        C = [0] * l
        for i in range(l):
            if arr[A[i]]:
                curr += 1
            else:
                arr[A[i]] = True
            if arr[B[i]]:
                curr += 1
            else:
                arr[B[i]] = True
            C[i] = curr
        return C
            