from collections import Counter

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d = Counter(nums)

        for value in d.values():
            if value % 2 == 1:
                return False
        
        return True
        