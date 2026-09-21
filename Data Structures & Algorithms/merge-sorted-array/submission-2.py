# doing this solution again to understand it fully

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i = m - 1 # highest n1 (non-zero)
        j = n - 1 # highest n2
        k = (m + n) - 1 # highest n1 (last 0)

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            
            k -= 1
        
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        
