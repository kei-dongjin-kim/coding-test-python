class Solution:
    def splitNum(self, num: int) -> int:
        num1, num2 = 0, 0
        list_num = []
        while num > 0:
            rest = num % 10
            list_num.append(rest)
            num //= 10
        list_num.sort()
        for i in range(len(list_num)):
            if i % 2 == 0:
                num2 = num2 * 10 + list_num[i]
            else:
                num1 = num1 * 10 + list_num[i]
        return num1 + num2