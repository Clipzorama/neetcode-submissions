# Time: O(n * k) - each of the n windows may slice/convert up to k digits
# Space: O(n + k) - string representation of num + current substring

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        # Convert num to a string so we can examine k-sized digit windows
        s = str(num)

        # Track how many k-sized substrings evenly divide num
        count = 0

        # Iterate through every valid starting position for a window of size k
        for i in range(len(s) - k + 1):

            # Extract the current k-sized window and convert it to an integer
            val = int(s[i:i + k])

            # Skip zero because division/modulo by zero is invalid
            if val == 0:
                continue

            # Count the window if it divides num with no remainder
            if num % val == 0:
                count += 1

        # Return the total number of divisor substrings
        return count


# Arguments to run the code
solution = Solution()

print(solution.divisorSubstrings(30003, 3))  # 1
print(solution.divisorSubstrings(240, 2))    # 2