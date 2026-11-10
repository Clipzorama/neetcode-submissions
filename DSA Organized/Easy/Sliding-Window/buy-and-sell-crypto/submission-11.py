class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxC = 0

        while right <= len(prices) - 1:
            if prices[left] <= prices[right]:
                maxC = max(maxC, prices[right] - prices[left])
            else:
                left = right

            right += 1
            
        return maxC