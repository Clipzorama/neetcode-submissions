# another very simple solution as well

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minBuy = prices[0]
        maxP = 0

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        

        return maxP