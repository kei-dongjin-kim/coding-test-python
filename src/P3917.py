class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        l = len(nums)
        res = [0] * l
        odd, even = 0, 0
        for i in range(l - 1, -1, -1):
            if nums[i] & 1:
                res[i] = odd
                even += 1
            else:
                res[i] = even
                odd += 1
        return res