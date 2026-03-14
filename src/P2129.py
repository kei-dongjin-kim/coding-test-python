class Solution:
    def capitalizeTitle(self, title: str) -> str:
        splited = title.split()
        l = len(splited)
        for i in range(l):
            curr = splited[i]
            if len(curr) <= 2:
                splited[i] = curr.lower()
            else:
                splited[i] = curr.capitalize()
        return " ".join(splited)