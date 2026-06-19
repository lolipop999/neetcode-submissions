class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy at the lowest price and sell at the highest price
        maxProfit = 0
        lowestPrice = prices[0]
        highestPrice = prices[0]

        for price in prices:
            if price > highestPrice:
                highestPrice = price
                maxProfit = max(maxProfit, highestPrice - lowestPrice)
            if (price < lowestPrice):
                lowestPrice = price
                highestPrice = lowestPrice
        return maxProfit
        