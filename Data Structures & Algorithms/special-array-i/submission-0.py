class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        l = 0
        j = 1
    
        while j < len(nums):

            if nums[l] % 2 == 0 and nums[j] % 2 == 0:
                return False
            
            elif nums[l] % 2 == 1 and nums[j] % 2 == 1:
                return False
            
            else:
                l += 1
                j += 1
        
        return True
        