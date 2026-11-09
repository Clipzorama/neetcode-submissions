class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        N = len(needle)
        left = 0

        if haystack == needle:
            return 0

        for right in range(N, len(haystack) + 1):
            curr_s = "".join(haystack[left:right])

            if curr_s == needle:
                return left

            left += 1
        
        return -1 

        