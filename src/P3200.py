class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:

        def helper(odd: int, even: int) -> int:
            cnt = 1
            while True:
                if cnt % 2 == 0:
                    even -= cnt
                    if odd >= cnt + 1:
                        cnt += 1
                    else:
                        break
                else:
                    odd -= cnt
                    if even >= cnt + 1:
                        cnt += 1
                    else:
                        break
            return cnt

        return max(helper(red, blue), helper(blue, red))