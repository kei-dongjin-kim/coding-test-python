class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        # ans = []
        # for arr in matrix:
        #     ans.append(sum(arr))
        # return ans

        return [sum(arr) for arr in matrix]