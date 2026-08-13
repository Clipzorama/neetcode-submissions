class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lstSet = set(nums)
        longest = 0

        for n in nums:

            # lets us know to start back to the beginning if the number is not 
            # consecutively incrementing

            if (n - 1) not in lstSet:
                length = 0
            # n + length, counts the first number and continues until incremented n 
            # in nums is not in the set
                while (n + length) in lstSet:
                    length += 1
            
                # we get the longest value after everything is scanned to return it.
                longest = max(length, longest)

        return longest