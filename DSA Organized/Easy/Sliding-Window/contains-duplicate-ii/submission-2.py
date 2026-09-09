class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0

        right = 1

        if k == 0:
            return False

        while right < len(nums):
            if nums[left] == nums[right] and abs(left - right) <= k:
                return True
            right += 1

            while abs(left - right) > k:
                left += 1
                right = left + 1

        return False