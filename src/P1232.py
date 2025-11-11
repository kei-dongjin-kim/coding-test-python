from typing import List

class Solution:
  def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
    # extract the first two points as a reference line
    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]

    # iterate over the remaining point to check
    for x, y in coordinates[2:]:
      # use cross product to prevent dividing zero
      if (x - x1) * (y2 - y1) != (y - y1) * (x2 - x1):
        return False
    
    return True
