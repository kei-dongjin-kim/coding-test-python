class Solution:
  def checkZeroOnes(self, s: str) -> bool:
    max0 = 0
    max1 = 0
    freq = 1
    previous = s[0]

    for i in range(1, len(s)):
      if previous == s[i]:
        freq += 1
      else:
        if previous == "0":
          max0 = max(max0, freq)
        else:
          max1 = max(max1, freq)
        freq = 1
      previous = s[i]

    if previous == "0":
      max0 = max(max0, freq)
    else:
      max1 = max(max1, freq)

    return max0 < max1