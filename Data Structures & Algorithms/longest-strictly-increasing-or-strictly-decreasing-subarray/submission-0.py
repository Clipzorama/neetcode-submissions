class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maxStrict = 0

        


        # First strictly increasing
        countI = 1
        maxI = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                countI += 1
                maxI = max(maxI, countI)
            else:
                countI = 1



        # Then strictly decreasing
        countD = 1
        maxD = 1

        for i in range(1, len(nums)):

            if nums[i] < nums[i - 1]:
                countD += 1
                maxD = max(countD, maxD)
            else:
                countD = 1
        

        return max(maxI, maxD)






        