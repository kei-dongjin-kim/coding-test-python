class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        words = sentence.split()
        for i in range(len(words)):
            tmp = words[i]
            if tmp[0] not in vowels:
                l = len(tmp)
                if l > 1:
                    tmp = tmp[1:l] + tmp[0]
            tmp += 'ma'
            for _ in range(i + 1):
                tmp += 'a'
            words[i] = tmp
        return ' '.join(words)