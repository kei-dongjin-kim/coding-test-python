class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        [left, right] = p.split("*")
        left_idx = s.find(left)
        if left_idx == -1:
            return False
        right_idx = s[left_idx + len(left):].find(right)
        if right_idx == -1:
            return False
        return True
