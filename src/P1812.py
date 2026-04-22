class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x = ord(coordinates[0]) - ord('a') + 1
        y = int(coordinates[1])
        bx = x % 2 == 0
        by = y % 2 == 0
        if (
            (bx == True and by == False) or
            (bx == False and by == True)
        ):
            return True
        return False