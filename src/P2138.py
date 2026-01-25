from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans: List[str] = []
        n = len(s)
        for i in range(0, n, k):
            ans.append(s[i:i + k])
        if len(ans[-1]) != k:
            ans[-1] += fill * (k - len(ans[-1]))
        return ans