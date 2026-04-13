class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        if not word.isalnum():
            return False

        vowel = 'aeiouAEIOU'

        if not any(w in vowel for w in word):
            return False
        
        if not any(w.isalpha() and w not in vowel for w in word):
            return False
        
        return True
