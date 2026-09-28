# Time: O(n log n) - sorting dominates; the two-pointer traversal is O(n)
# Space: O(1) auxiliary space - pointers and variables use constant extra space
# Optimal Approach: Sorting + Greedy + Two Pointers

class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        # Track the current score
        score = 0

        # Sort tokens so cheapest is left and most expensive is right
        tokens.sort()

        # Initialize two pointers at both ends of the array
        l, r = 0, len(tokens) - 1

        # Continue while there are still tokens available
        while l <= r:

            # Play the cheapest token face-up if we have enough power
            if tokens[l] <= power:
                power -= tokens[l]
                score += 1
                l += 1

            # Trade one score for the most power using the largest token
            elif score >= 1 and l != r:
                power += tokens[r]
                score -= 1
                r -= 1

            # Stop if we cannot play any token face-up or face-down
            else:
                break

        # Return the maximum score achieved
        return score






result = Solution()

# t = [100]
# p = 50

# tt = [100,200,300,400]
# pp = 200

# ttt = [200,100]
# ppp = 150

a = [48,87,26]
b = 81

# print(result.bagOfTokensScore(t, p))
# print(result.bagOfTokensScore(tt, pp))
# print(result.bagOfTokensScore(ttt, ppp))

print(result.bagOfTokensScore(a, b))


