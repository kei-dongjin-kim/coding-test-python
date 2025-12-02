class Solution:
  def sumAndMultiply(self, n: int) -> int:
    x = 0
    m = 0
    while n > 0:
      rest = n % 10
      if rest != 0:
        x += rest * (10 ** m)
        m += 1
      n //= 10
    x1 = x
    sum = 0
    while x1 > 0:
      rest = x1 % 10
      sum += rest
      x1 //= 10
    return x * sum