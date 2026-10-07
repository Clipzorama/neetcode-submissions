# the sliding window solution

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        # this one is alot more simpler and we're using a set which comes in handy with the sliding window.

        for right in range(len(nums)):
            if nums[right] in window:
                return True
            
            window.add(nums[right])

            # this basically keeps the same contrain of i - j <= k
            if len(window) > k:
                window.remove(nums[right - k])
        
        return False
        