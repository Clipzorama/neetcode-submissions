# Time: O(n)
# Space: O(1)

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # original variable
        minLength = float("inf")
        curr_length = 0
        curr_sum = 0
        
        # left will be the window we have and will shrink if applicable
        left = 0
        
        
        for right in range(len(nums)):
            # add from nums[right]
            curr_sum += nums[right]

            # as long as this condition holds, we will record the length and then shrink to see if
            # condition is still applicable
            while curr_sum >= target:
                curr_length = right - left + 1
                minLength = min(minLength, curr_length)
                # here we shrink the window and continue to see if condition still holds
                curr_sum -= nums[left]
                left += 1
        
        # if minLength never updates, then we will return 0
        if minLength == float("inf"): return 0
        
        return minLength
