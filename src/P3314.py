from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for a in nums:
            flag = True
            for b in range(1, a):
                if b | b + 1 == a:
                    ans.append(b)
                    flag = False
                    break
            if flag:
                ans.append(-1)
        return ans