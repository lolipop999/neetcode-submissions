class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxProfit = 0
        for i in range(1, len(prices)):
            if (prices[i] < prices[l]):
                l = i
            else:
                maxProfit = max(maxProfit, prices[i] - prices[l])
        return maxProfit
            