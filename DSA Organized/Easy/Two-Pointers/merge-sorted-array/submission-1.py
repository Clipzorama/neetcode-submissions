class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # another attempt of doing this solution to understand the pattern 

        i = m - 1 # highest number in nums1
        j = n - 1 # highest number in nums2
        k = m + n - 1 # last 0 in nums1 (we will be progressing down)

        while i >= 0 and j >= 0:
            # added the highest numbers to the top of 0
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            
            k -= 1
        
        # just incase theres some left inside of nums2
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        



        