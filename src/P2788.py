from typing import List

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans: List[str] = []
        for w in words:
            curr: str = ""
            for c in w:
                if c == separator:
                    if curr != "":
                        ans.append(curr)
                        curr = ""
                else:
                    curr += c
            if curr != "":
                ans.append(curr)
        return ans