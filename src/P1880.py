class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        
        def helper(word: str) -> int:
            res = 0
            for c in word:
                curr = ord(c) - ord('a')
                res = res * 10 + curr
            return res
        
        f = helper(firstWord)
        s = helper(secondWord)
        t = helper(targetWord)

        return f + s == t