class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l = len(num)
        max_idx = -1
        max_val = -1
        for i in range(l - 2):
            if num[i] == num[i + 1] and num[i + 1] == num[i + 2]:
                curr = int(num[i:i + 3])
                if max_val < curr:
                    max_val = curr
                    max_idx = i
        if max_idx == -1:
          return ""
        return num[max_idx:max_idx + 3]