from typing import List

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words)
        ans: List[str] = [words[0]]
        sorted1 = sorted(words[0])
        previous = "".join(sorted1)
        for i in range(1, n):
            sorted1 = sorted(words[i])
            curr = "".join(sorted1)
            if previous == curr:
                continue
            else:
                ans.append(words[i])
            previous = curr
        return ans