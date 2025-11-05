class Solution:
  def reverseDegree(self, s: str) -> int:
    res = 0
    index = 1
    for c in s:
      # Calculate the postion of the character
      # 0 for 'a', 25 for 'z'
      val = ord(c) - ord('a')
      # Add the weighted reversed value (26 - val) * index
      res += (26 - val) * index
      index += 1
    return res