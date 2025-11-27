from typing import List
from collections import Counter

class Solution:
    def oddString(self, words: List[str]) -> str:
        arr = []
        for i in range(len(words)):
            out = ""
            for j in range(1, len(words[i])):
                out += str(ord(words[i][j]) - ord(words[i][j - 1]))
                out += ","
            arr.append(out)
        count = Counter(arr)
        target = ""
        for key, val in count.items():
            if val == 1:
                target = key
        
        for i in range(len(arr)):
            if arr[i] == target:
                return words[i]
        
        return ""