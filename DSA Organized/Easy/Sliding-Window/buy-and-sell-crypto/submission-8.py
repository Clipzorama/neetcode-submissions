# time: O(n)
# space: O(1) -> since you are updating the profit value and incrementing left and right


# Two pointer solution

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        profit = 0

        while right <= len(prices) - 1:
            if prices[left] <= prices[right]:
                profit = max(profit, prices[right] - prices[left])
            else:
                left = right
            
            right += 1
        
        return profit 
        