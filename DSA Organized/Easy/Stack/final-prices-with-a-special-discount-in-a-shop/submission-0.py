# time: O(n)
# space: O(n)

class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        # Copy prices so discounted values can be updated without changing the original list
        result = prices[:]

        # Store indices of prices still waiting for their first smaller-or-equal discount
        stack = []

        for i in range(len(prices)):

            # Current price discounts every previous waiting price that is >= it
            while stack and prices[stack[-1]] >= prices[i]:
                result[stack.pop()] -= prices[i]

            # Current price now waits for its own future discount
            stack.append(i)
        
        return result


res = Solution()
p = [8,4,6,2,3]
print(res.finalPrices(p))
