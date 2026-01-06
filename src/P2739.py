class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        distance: int = 0
        while mainTank > 0:
            if mainTank >= 5:
                distance += 5 * 10
                if additionalTank > 0:
                    mainTank -= 4
                    additionalTank -= 1
                else:
                    mainTank -= 5
            else:
                distance += mainTank * 10
                mainTank = 0
                break
        return distance