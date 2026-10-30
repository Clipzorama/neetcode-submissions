# practice to understand the pattern recognition

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}


        for i in range(len(nums2)):

            curr = nums2[i]

            # monotonic decreasing stack
            while stack and stack[-1] < curr:
                num = stack.pop()
                next_greater[num] = curr
            
            stack.append(curr)
        
        return [next_greater.get(num, -1) for num in nums1]