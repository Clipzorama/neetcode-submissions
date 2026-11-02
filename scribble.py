from typing import List

# circular array solution

class Solution:
    def check(self, nums: List[int]) -> bool:
        N = len(nums)
        count = 1
        # 2 * N --> makes the array circular [3, 4, 5, 1, 2, 3, 4, 5, 1, 2]
        for i in range(1, 2 * N):

            if nums[(i - 1) % N] <= nums[i % N]:
                count += 1

            if count == N:
                return True

        return False
        






n = [3, 4, 5, 1, 2]
result = Solution()
print(result.check(n))