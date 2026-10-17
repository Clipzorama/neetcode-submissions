class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prenum = prices[0]
        maxPrice = 0

        for i in range(1, len(prices)):
            if prices[i] <= prenum:
                prenum = prices[i]
            else:
                maxPrice = max(maxPrice, prices[i] - prenum)
        
        return maxPrice