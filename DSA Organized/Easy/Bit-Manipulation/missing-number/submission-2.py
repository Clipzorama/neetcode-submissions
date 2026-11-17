# Having to use XOR in this operation


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums) + 1

        for i, num in enumerate(nums, start=1):
            res ^= i
            res ^= num
        
        return res



result = Solution()
print(result.missingNumber([1, 2, 3, 5, 6]))