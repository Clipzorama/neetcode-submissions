# theres also the prefix num solution

# time: O(n)
# space: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prenum = prices[0]
        maxP = 0

        # very similar to the two pointer solution
        for i in range(1, len(prices)):
            if prices[i] < prenum:
                prenum = prices[i]
            else:
                maxP = max(maxP, prices[i] - prenum)
        
        return maxP
    