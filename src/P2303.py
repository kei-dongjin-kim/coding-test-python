from typing import List

class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax: float = 0.0

        if income <= 0:
            return tax

        n = len(brackets)

        if income < brackets[0][0]:
            tax += income * brackets[0][1] * 0.01
            income -= income
        else:
            tax += brackets[0][0] * brackets[0][1] * 0.01
            income -= brackets[0][0]

        for i in range(1, n):
            if income <= 0:
                break
            curr = brackets[i][0] - brackets[i - 1][0]
            if income < curr:
                tax += income * brackets[i][1] * 0.01
                break
            else:
                tax += curr * brackets[i][1] * 0.01
                income -= curr

        return tax