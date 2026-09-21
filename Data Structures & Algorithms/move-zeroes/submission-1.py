class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        write = 0

        # until whatever value of write, we will have all the elements that are non-zeros
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1
        
        # anything after that, we will add a zero until the list reaches the adequate size
        for i in range(write, len(nums)):
            nums[i] = 0

        
        
        