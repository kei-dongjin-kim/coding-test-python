class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        cnt = 0
        words = text.split()
        for w in words:
            flag = True
            for c in list(w):
                if c in brokenLetters:
                    flag = False
                    break
            if flag:
                cnt += 1
        return cnt