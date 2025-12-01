from typing import List

class Solution:
  def minMoves(self, nums: List[int]) -> int:
    max_val = max(nums)
    total = sum(nums)
    return max_val * len(nums) - total