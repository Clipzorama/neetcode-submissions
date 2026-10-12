# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        maxL = 0

        v = ["a", "e", "i", "o", "u"]

        for i in range(k):
            if s[i] in v:
                count += 1
        maxL = max(maxL, count)

        for i in range(k, len(s)):
            if s[i - k] in v:
                count -= 1

            if s[i] in v:
                count += 1
            
            maxL = max(maxL, count)
        
        return maxL


result = Solution()
print(result.maxVowels("weallloveyou", 7))