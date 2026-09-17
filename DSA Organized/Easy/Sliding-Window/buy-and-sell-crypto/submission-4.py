# Two Pointer Solution 

# time complextiy: O(n)
# space complexity: O(1)


# pretty self explanatory. just read the code

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = 0
        right = 1
        maxP = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxP = max(maxP, profit)
            else:
                # Move left to right because we found a cheaper/better buying price.
                # The old left is no longer useful for maximizing future profit.    
                left = right

            right += 1

        return maxP
        
# Input: prices = [10,1,5,6,7,1]

# Output: 6