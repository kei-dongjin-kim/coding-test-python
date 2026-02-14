from typing import List

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        lr = len(mat)
        lc = len(mat[0])
        for ir in range(lr):
            if ir % 2 == 0:
                for ic in range(lc):
                    shifted = (ic + lc - k) % lc
                    if mat[ir][ic] != mat[ir][shifted]:
                        return False
            else:
                for ic in range(lc):
                    shifted = (ic + k) % lc
                    if mat[ir][ic] != mat[ir][shifted]:
                        return False
        return True