class Solution:
    def generateTag(self, caption: str) -> str:
        list1 = caption.split()
        res = "#"
        if len(list1) == 0:
            return res
        res += list1[0].lower()
        for item in list1[1:]:
            res += item.capitalize()
        return res[:100]
