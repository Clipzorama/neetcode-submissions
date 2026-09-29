# MOST OPTIMAL SOLUTION

# Time: O(n log n). --> Sorting + two-pointer traversal
# Space: O(1) auxiliary space
class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        res = 0
        mod = 10**9 + 7

        # Sort so each index can act as the minimum and the right pointer as the maximum.
        nums.sort()

        # Start r at the largest possible maximum.
        r = len(nums) - 1

        for i, left in enumerate(nums):

            # Shrink r until nums[i] + nums[r] satisfies the target condition.
            while i <= r and left + nums[r] > target:
                r -= 1

            # If a valid range exists, nums[i] is fixed as the minimum.
            if i <= r:

                # Every element between i+1 and r can be included or excluded, giving 2^(r-i) subsequences.
                res += 2 ** (r - i)

                # Keep the answer within the required modulo.
                res %= mod

        # Return the total number of valid non-empty subsequences.
        return res