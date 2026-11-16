# time: O(n)
# space: O(m)


class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Track characters that currently have an unmatched occurrence
        seen = set()

        # Count the total characters that can form symmetric pairs
        res = 0

        # Process each character and greedily form pairs when possible
        for char in s:

            # A match means we can form a complete pair
            if char in seen:

                # Remove the character since its unmatched occurrence is paired
                # since we're not adding the second one in, we can just take out the first one
                seen.remove(char)

                # Each completed pair contributes 2 characters to the palindrome
                res += 2

            else:
                # Store this character until another occurrence completes its pair
                seen.add(char)

        # Add one center character if any unmatched characters remain
        return res + 1 if seen else res
