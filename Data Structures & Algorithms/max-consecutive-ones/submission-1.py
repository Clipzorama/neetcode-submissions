class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones = 0
        maxO = ones


        for i in range(len(nums)):

            if nums[i] == 1:
                ones += 1
                maxO = max(maxO, ones)
            else:
                ones = 0
        
        return maxO