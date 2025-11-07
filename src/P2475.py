class Solution:
  def unequalTriplets(self, nums):
    length = len(nums)
    count = 0

    # iterate over all combinations of three district indices (i, j, k)
    for i in range(length - 2):
      for j in range(i + 1, length - 1):
        if nums[i] == nums[j]:
          continue
        for k in range(j + 1, length):
          # check that all three numbers are different
          if nums[j] != nums[k] and nums[k] != nums[i]:
            count += 1
        
    return count