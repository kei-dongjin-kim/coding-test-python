class Solution:
    def possibleStringCount(self, word: str) -> int:
        left, right = 0, 1
        count = 1
        length = len(word)
        while right < length:
            if word[left] == word[right]:
                count += 1
            left += 1
            right += 1
        
        return count