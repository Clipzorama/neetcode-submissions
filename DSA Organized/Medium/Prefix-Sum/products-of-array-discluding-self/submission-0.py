"""
PREFIX 

[1, 1, 1, 1] Iteration 1 (since 1 is assigned to prefix = 1 by default)
[1, 1, 1, 1] Iteration 2 (since 1 is assigned to prefix = 1 after multiplication = 1 times 1 -> nums[0])
[1, 1, 2, 1] Iteration 3 (since 2 is assigned to prefix = 2 after multiplication with selected array = 1 times 2 -> nums[1])
[1, 1, 2, 8] Iteration 4 (since 8 is assigned to prefix = 8 after multiplication with selected array = 2 times 4 -> nums[2])

"""



"""
SUFFIX

[1, 1, 2, 8] Iteration 1 (since 8 times 1 --> suffix then equal 6)
[1, 1, 12, 8] Iteration 2 (since 2 times 6 --> suffix then equal 24)
[1, 1, 2, 8] Iteration 3 (since 1 times 24 --> suffix then equal 48)
[1, 1, 2, 8] Iteration 4 (since 1 times 48 --> LOOP BREAKS AND ANSWER IS RETURNED)

"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1

        # this portion assigns each element the product on the left despite the       
        # current i so --> [1, 1, 2, 8]

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        suffix = 1

        # Example above of iteration

        for i in range(len(nums) -1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res








