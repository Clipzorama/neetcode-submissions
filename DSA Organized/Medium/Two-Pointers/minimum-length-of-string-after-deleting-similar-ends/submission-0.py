# optimal solution

# time: O(n)
# space: O(1)

class Solution:
    def minimumLength(self, s: str) -> int:
        # Two pointers track the current remaining substring.
        left = 0
        right = len(s) - 1

        # We can remove characters only when both ends contain the same character.
        while left < right and s[left] == s[right]:

            # Save the matching boundary character so we can remove all copies of it from both ends.
            c = s[left]

            # Remove every occurrence of c from the left side.
            while left <= right and s[left] == c:
                left += 1

            # Remove every occurrence of c from the right side.
            while left <= right and s[right] == c:
                right -= 1

        # Whatever remains between the two pointers is the minimum possible length.
        return right - left + 1