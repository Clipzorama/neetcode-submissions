class Solution:
    # Time Complexity: O(N) - Each index is pushed and popped at most once.
    # Space Complexity: O(N) - Stack and result array can each hold N elements.

    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        N = len(nums)
        stack = []  # Stores indices waiting for their next greater element
        res = [-1] * N  # Default to -1 if no greater element exists

        # Traverse twice to handle the circular array
        for i in range(2 * N):
            curr = nums[i % N]  # Modulo wraps the index back to 0 after reaching N

            # Pop elements whose next greater value is the current element
            while stack and nums[stack[-1]] < curr:
                idx = stack.pop()  # Remove the index that found its next greater element
                res[idx] = curr  # Store the next greater value at that index

            # Only push indices during the first traversal to avoid duplicates
            if i < N:
                stack.append(i)

        return res