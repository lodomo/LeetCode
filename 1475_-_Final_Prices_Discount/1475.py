class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i, num in enumerate(prices):
            for j in range(i + 1, len(prices)):
                if prices[j] <= num:
                    prices[i] -= prices[j]
                    break
        return prices
