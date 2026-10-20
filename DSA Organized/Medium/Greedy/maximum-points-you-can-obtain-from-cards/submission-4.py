
from typing import List

# Time Complexity: O(k)
# - Summing the first k cards and performing k exchanges each take O(k) time.

# Space Complexity: O(k)
# - Slicing cardPoints[:k] creates a temporary list of k elements.

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        # Start by selecting the first k cards from the left
        current_sum = sum(cardPoints[:k])

        # Initialize the maximum score with the initial sum
        maxS = current_sum

        # Perform k exchanges until 0 selected cards remain on the left
        for i in range(1, k + 1):

            # Remove cards from the left selection (indices k-1 to 0)
            current_sum -= cardPoints[k - i]

            # Add cards from the right end (indices -1, -2, -3, ...)
            current_sum += cardPoints[-i]

            # Track the maximum score across all valid combinations
            maxS = max(maxS, current_sum)

        # Return the maximum score after checking all k+1 combinations
        return maxS
