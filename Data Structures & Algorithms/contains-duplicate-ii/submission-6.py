class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        left = 0

        for right in range(len(nums)):
            # this code is the most important part as it checks if the problem is within the required window of k
            if abs(left - right) > k:
                window.remove(nums[left])
                left += 1

            # if window is satisfied and duplication is detected, we return True
            if nums[right] in window:
                return True

            window.add(nums[right])
        
        return False