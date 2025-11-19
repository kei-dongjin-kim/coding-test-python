from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        for left in range(0, n, 3):
            seen = set()
            flag = True
            # 슬라이싱 없이 인덱스로 확인
            for i in range(left, n):
                if nums[i] in seen:
                    flag = False
                    break
                seen.add(nums[i])
            if flag:
                return count
            count += 1
        return count
