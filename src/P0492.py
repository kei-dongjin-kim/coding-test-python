import math
from typing import List

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        sq = int(math.sqrt(area))
        for W in range(sq, 0, -1):
            if area % W == 0:
                return [area // W, W]
