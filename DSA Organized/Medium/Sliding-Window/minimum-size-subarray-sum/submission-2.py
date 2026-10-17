# Time Complexity: O(n)
# - The right pointer traverses the array once: O(n).
# - The left pointer only moves forward, at most n times: O(n).
# - Although the while loop is nested, it executes at most n times
#   TOTAL, not n times per iteration of the for loop.
# - Total: O(n) + O(n) = O(n).


# Space Complexity: O(1)
# - Only a fixed number of variables are used.
# - No additional data structures grow with the input size.

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = float("inf")
        currLength = 0
        left = 0
        currSum = 0

        # add from the right
        for right in range(len(nums)):
            currSum += nums[right]

            # shrink the window until currSum is less than target
            while currSum >= target:
                currLength = right - left + 1
                minLength = min(minLength, currLength)
                currSum -= nums[left]
                left += 1

        if minLength == float("inf"): return 0

        return minLength