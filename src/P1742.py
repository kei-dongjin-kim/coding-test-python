class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        ball = {}
        for n in range(lowLimit, highLimit + 1):
            sum_dgt = 0
            while n > 0:
                rest = n % 10
                sum_dgt += rest
                n //= 10
            ball[sum_dgt] = ball.get(sum_dgt, 0) + 1
        return max(ball.values())