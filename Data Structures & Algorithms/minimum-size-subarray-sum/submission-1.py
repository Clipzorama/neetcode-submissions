# time: O(n)
# space: O(1)

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