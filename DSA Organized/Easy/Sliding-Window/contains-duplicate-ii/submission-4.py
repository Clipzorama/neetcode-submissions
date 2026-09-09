class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        for right in range(len(nums)):
            if nums[right] in window:
                return True

            window.add(nums[right])

            if len(window) > k:
                window.remove(nums[right - k])

        return False