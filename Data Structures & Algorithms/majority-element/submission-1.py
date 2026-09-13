from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = Counter(nums)
        condition = len(nums) // 2

        for key, value in n.items():
            if value > condition:
                return key
        
        return -1
