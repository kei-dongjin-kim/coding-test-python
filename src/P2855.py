from typing import List
class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums)
        a_cnt = 0
        b_cnt = -1

        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                a_cnt += 1
                b_cnt = n - i

        if nums[0] < nums[n - 1]:
            a_cnt += 1
            b_cnt = 0
        
        if a_cnt == 1:
            return b_cnt
        elif a_cnt == 0:
            return 0
        else:
            return -1
