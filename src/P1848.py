class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        n = len(nums)
        left = start
        right = start

        while left >= 0 or right < n:
            if left >= 0 and nums[left] == target:
                return abs(start - left)
            if right < n and nums[right] == target:
                return abs(right - start)
            left -= 1
            right += 1

        return -1