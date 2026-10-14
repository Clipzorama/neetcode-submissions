class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        setter = set()

        for num in nums:
            if num in setter:
                return True
            
            setter.add(num)
        
        return False