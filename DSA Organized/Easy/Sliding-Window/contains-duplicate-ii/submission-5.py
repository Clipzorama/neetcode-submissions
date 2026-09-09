# Time Complexity: O(n) average
# Space Complexity: O(n)

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        # this one is alot more simpler and we're using a set which comes in handy with the sliding window.

        for right in range(len(nums)):
            if nums[right] in window:
                return True

            # if not duplicate we add
            window.add(nums[right])

            # but we make sure that it satisfies the requirement
            if len(window) > k:
                window.remove(nums[right - k])

        return False
