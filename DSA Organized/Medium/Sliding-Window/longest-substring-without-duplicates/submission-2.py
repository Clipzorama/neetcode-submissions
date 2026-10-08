# sliding window solution

# Given a string s, find the length of the longest substring without duplicate characters.

# A substring is a contiguous sequence of characters within a string.


# Time: O(n)
# Space: O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # its better to use a set here instead of a array as worst case can lead to O(n²) with:
        # s[right] in res # O(k)
        # res.remove(s[left])  # O(k)

        window = set()
        left = 0
        currLength = 0
        maxLength = float("-inf")

        for right in range(len(s)):

            # first we check for duplicates 
            while s[right] in window:
                window.remove(s[left])
                left += 1

            # then we add into the set
            window.add(s[right])

            currLength = right - left + 1
            maxLength = max(maxLength, currLength)
        
        if maxLength == float("-inf"): return 0

        return maxLength