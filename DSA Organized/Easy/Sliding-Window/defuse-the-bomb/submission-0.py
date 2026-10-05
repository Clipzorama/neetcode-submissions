from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        N = len(code)                 # Store the length of the circular array
        res = [0] * N                 # Create the result array filled with zeros

        l = 0                         # Left pointer of the sliding window
        cur_sum = 0                   # Track the sum of the current window

        for r in range(N + abs(k)):   # Move right far enough to handle circular wraparound
            cur_sum += code[r % N]    # Add the newest value into the window

            if r - l + 1 > abs(k):    # Shrink the window if it becomes larger than |k|
                cur_sum -= code[l % N] # Remove the leftmost value from the window
                l = (l + 1) % N       # Move the left pointer forward circularly

            if r - l + 1 == abs(k):   # Process the sum once the window has exactly |k| values
                if k > 0:             # Positive k means the window represents the next k values
                    res[(l - 1) % N] = cur_sum  # Store the sum for the element before the window

                elif k < 0:           # Negative k means the window represents the previous |k| values
                    res[(r + 1) % N] = cur_sum  # Store the sum for the element after the window

        return res                    # Return the decrypted array
            
        