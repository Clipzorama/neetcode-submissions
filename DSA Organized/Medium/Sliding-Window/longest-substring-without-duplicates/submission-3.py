class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        currLength = 0
        maxLength = 0
        left = 0

        for right in range(len(s)):

            while s[right] in window:
                window.remove(s[left])
                left += 1
            
            window.add(s[right])

            currLength = right - left + 1
            maxLength = max(maxLength, currLength)
        
        return maxLength



