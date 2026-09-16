class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = m - 1 # references the highest num in num1
        j = n - 1 # references the highest num in num2
        k = m + n - 1 # references the last 0

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1
        
        # whatever is left in nums2 will go in the last elements of k. starting from its 
        # highest number and decrements from there
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        