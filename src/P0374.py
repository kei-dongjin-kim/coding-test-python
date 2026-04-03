# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    
    THE_NUMBER_THAT_I_PICKED = 10


    def guess(self, num: int) -> int:
        if num > self.THE_NUMBER_THAT_I_PICKED:
            return -1
        elif num < self.THE_NUMBER_THAT_I_PICKED:
            return 1
        else:
            return 0
        

    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while left < right:
            res = self.guess(n)
            if res == -1:
                right = n
            elif res == 1:
                left = n
            elif res == 0:
                break
            n = (left + right) // 2
        return n