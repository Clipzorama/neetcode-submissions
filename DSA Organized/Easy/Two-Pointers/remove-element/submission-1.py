# read-write approach two pointer solution 

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write = 0
        # just another practice run doing this solution with two pointers
        for read in range(len(nums)):
            if nums[read] != val:
                nums[write] = nums[read]
                write += 1
        
        return len(nums[:write])