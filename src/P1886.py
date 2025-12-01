from typing import List

class Solution:
  def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
    for _ in range(4):
      if mat == target:
        return True
      else:
        mat = self.rotate(mat)
    return False
  def rotate(self, mat: List[List[int]]) -> List[List[int]]:
    res = []
    n = len(mat)
    for col in range(n):
      new_row = []
      for row in range(n - 1, -1, -1):
        new_row.append(mat[row][col])
      res.append(new_row)
    return res