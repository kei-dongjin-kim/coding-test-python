from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        count = 0
        while len(nums) > 1:
            flag = False
            for i in range(1, len(nums)):
                if nums[i - 1] > nums[i]:
                    flag = True
            
            if flag:
                min_idx = 1
                min_val = nums[0] + nums[1]
                for i in range(2, len(nums)):
                    curr_sum = nums[i - 1] + nums[i]
                    if curr_sum < min_val:
                        min_idx = i
                        min_val = curr_sum

                new_arr = nums[0:min_idx - 1]
                new_arr += [min_val]
                new_arr += nums[min_idx + 1:]
                nums = new_arr
                count += 1
            else:
                break

        return count