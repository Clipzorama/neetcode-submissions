class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

    # monotonic decreasing stack
        stack = []
        next_greater = {}

        for i in range(len(nums2)):
            curr = nums2[i]

            # here we will be taking the element out of stack and adding the greater element in its 
            # value

            while stack and stack[-1] < curr:
                num = stack.pop()
                next_greater[num] = curr
            

            # we add the curr element as well have to check it as well
            stack.append(curr)
        
        return [next_greater.get(num, -1) for num in nums1]
