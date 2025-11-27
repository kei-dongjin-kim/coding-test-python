from typing import List

class Solution:
  def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
    max_key = divisors[0]
    max_val = 0
    for i in divisors:
      count = 0
      for j in nums:
        if j % i == 0:
          count += 1
      if max_val < count:
        max_key = i
        max_val = count
      elif max_val == count:
        if max_key > i:
          max_key = i
    return max_key