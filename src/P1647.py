class Solution:
    def minDeletions(self, s: str) -> int:
        list1 = []
        for e in set(s):
            list1.append(s.count(e))
        list1.sort(reverse=True)
        result = 0
        curr = list1[0]
        for n in list1[1:]:
            if curr <= 0:
                result += n
            elif curr <= n:
                val = n - curr + 1
                result += val
                curr = n - val
            else:
                curr = n
        return result
        