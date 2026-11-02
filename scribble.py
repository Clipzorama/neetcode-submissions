from typing import List


class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        N = len(nums)
        stack = []
        res = [-1] * len(nums)

        for i in range(1, 2 * N):
            curr = nums[i % N]

            while stack and nums[(i - 1) % N] < curr:
                idx = stack.pop()
                res[idx] = curr
            
            stack.append(i % N)
        
        return res
        
        






n = [1,2,3,4,3]
# Output: [2,3,4,-1,4]
result = Solution()
print(result.nextGreaterElements(n))