class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        total = 0
        maximum = 0

        for num in nums:
            if num == 1:
                total += 1
                maximum = max(maximum, total)
            else:
                total = 0
        
        return maximum