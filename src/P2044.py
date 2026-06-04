from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        def bitwiseor(li: list[int]) -> int:
            result = 0
            for l in li:
                result |= l
            return result

        res = []
        subset = []
        def dfs(i: int):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)
        dfs(0)

        max_val = -1
        freq = {}
        for subset in res:
            curr = bitwiseor(subset)
            max_val = max(max_val, curr)
            freq[curr] = freq.get(curr, 0) + 1

        return freq[max_val]
