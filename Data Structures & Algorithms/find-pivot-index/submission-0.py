class Solution:

    def pivotIndex(self, nums: List[int]) -> int:
        # Pattern: Prefix Sum / Running Sum
        # Time: O(n) | Space: O(1)

        leftSum = 0
        rightSum = 0
        total = sum(nums)

        # Treat each index as a potential pivot
        for i in range(len(nums)):

            # Remove the left sum and current element(pivot) to get the right sum
            rightSum = total - nums[i] - leftSum

            # A pivot exists when both sides have equal sums
            if leftSum == rightSum:
                return i

            # Add the current element to the left sum for the next index
            leftSum += nums[i]

        return -1
        