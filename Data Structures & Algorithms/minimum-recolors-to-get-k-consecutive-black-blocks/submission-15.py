
# SLIDING WINDOW APPROACH:
# r starts at k because the first k elements are already the first window.
# r = new element entering the window.
# l = r - k gives the old element leaving the window.


# Time Complexity: O(k) + O(n - k) ---> O(n)
# Space Complexity: O(1)


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        changes = 0
        minimum = 0

        # first window
        for i in range(k):
            if blocks[i] == "W":
                changes += 1

        minimum = changes
        print(minimum)

        # Now we slide the entire window

        # Keep in mind of how this window is structured. very important to learn this type of pattern
        for right in range(k, len(blocks)):
            l = right - k

            if blocks[l] == "W":
                changes -= 1

            if blocks[right] == "W":
                changes += 1

            minimum = min(minimum, changes)

        return minimum

