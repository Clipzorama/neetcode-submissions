

# Pattern: Prefix + Suffix (Combining Both Sides)
# When to recognize: A problem requires information from elements before AND after each index, often excluding the current element.

# Core intuition:

# - Prefix → Accumulate information from left to right.
# - Suffix → Accumulate information from right to left.
# - Combine → Use information from both sides to calculate the answer.

# ans[i] = prefix[i] * suffix[i]

from typing import List

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





n = [3, 2, 5, 4, 6]
result = Solution()

print(result.productExceptSelf(n))




