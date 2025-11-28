class Solution:
  def reverseStr(self, s: str, k: int) -> str:
    res = ""
    count = 0
    le = len(s)
    for i in range(0, le, k):
      right = i + k
      if i + k > le:
        right = le
      curr = s[i:right]
      if count % 2 == 0:
        curr = curr[::-1]
      res += curr
      count += 1
    return res