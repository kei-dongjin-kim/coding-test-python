class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        rest = purchaseAmount % 10
        purchaseAmount -= rest
        if rest >= 5:
            purchaseAmount += 10
        return 100 - purchaseAmount
