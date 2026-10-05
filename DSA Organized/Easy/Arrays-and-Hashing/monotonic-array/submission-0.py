# Time: O(n)
# Space: O(1)

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # Assume the array could be either increasing or decreasing
        increasing, decreasing = True, True

        # Compare each number with the one directly after it
        for i in range(len(nums) - 1):
            
            # If order decreases, it can no longer be monotonically increasing
            if not (nums[i] <= nums[i + 1]):
                increasing = False

            # If order increases, it can no longer be monotonically decreasing
            if not (nums[i] >= nums[i + 1]):
                decreasing = False
        
        # The array is monotonic if at least one direction stayed valid
        return increasing or decreasing