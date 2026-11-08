# PATTERN: Circular indexing + Josephus recurrence

# O(n) - Time
# O(1) - Space

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        # Start with index 0 since a single player is always the winner.
        winner = 0

        # Build up from 1 player to n players, updating the winner's position.
        for i in range(1, n + 1):

            # Shift the previous winner by k and use modulo to wrap around the circle.
            winner = (winner + k) % i

        # Convert the zero-based winning index to the player's actual number.
        return winner + 1