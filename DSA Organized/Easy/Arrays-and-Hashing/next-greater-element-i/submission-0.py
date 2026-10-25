from typing import List

# Monotonic Decreasing Stack
# Time: O(n + m) | Space: O(n)

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # Stores elements still waiting to find their next greater element
        stack = []

        # Maps each element to its next greater element
        next_greater = {}

        # Traverse nums2 from left to right
        for curr in nums2:

            # Keep popping while the current number is greater than the stack's top
            while stack and stack[-1] < curr:

                # Remove the smaller element because we've found its next greater element
                num = stack.pop()

                # Record the current number as the popped element's next greater element
                next_greater[num] = curr

            # Push the current number to wait for its own next greater element
            stack.append(curr)

        # Return answers in nums1 order, using -1 if no greater element was found
        return [next_greater.get(num, -1) for num in nums1]