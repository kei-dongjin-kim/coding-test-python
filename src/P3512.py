from typing import List

class Solution:
  def minOperations(self, nums: List[int], k: int) -> int:
    sum = 0
    for n in nums:
      sum += n
    return sum % k