class Solution:
    def scoreBalance(self, s: str) -> bool:
        left: int = 0
        l_sum: int = ord(s[left]) - 96
        right: int = len(s) - 1
        r_sum: int = ord(s[right]) - 96
        while left < right:
            if left + 1 == right and l_sum == r_sum:
                return True
            elif l_sum < r_sum:
                left += 1
                l_sum += ord(s[left]) - 96
            else:
                right -= 1
                r_sum += ord(s[right]) - 96
        return False