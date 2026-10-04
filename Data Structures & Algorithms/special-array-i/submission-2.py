# this is a cleaner way to do this problem but either way, but solutions are optimal
# time: O(n)
# space: O(1)

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i - 1] % 2 == nums[i] % 2:
                return False
        
        return True