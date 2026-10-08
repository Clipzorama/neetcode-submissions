# Time: O(n) - Initialize the first window, then slide through the string once.
# Space: O(1) - Only a constant number of variables are used.

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = 0

        # Count the white blocks in the first window of size k.
        for i in range(k):
            if blocks[i] == "W":
                count += 1

        # Initialize the minimum recolors using the first window.
        mChanges = count

        # Slide the window by moving the right pointer from index k onward.
        for right in range(k, len(blocks)):

            # Remove the outgoing white block's contribution from the count.
            if blocks[right - k] == "W":
                count -= 1

            # Add the incoming white block's contribution to the count.
            if blocks[right] == "W":
                count += 1

            # Track the minimum number of white blocks across all windows.
            mChanges = min(mChanges, count)

        return mChanges