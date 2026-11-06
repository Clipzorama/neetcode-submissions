# time: O(n)
# space: O(1)

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        count = nums[0]
        maxCount = count

        for i in range(1, len(nums)):

            if nums[i] > nums[i - 1]:
                count += nums[i]
                maxCount = max(maxCount, count)
            else:
                count = nums[i]
        
        return maxCount
