# this is a very easy way to do this problem. but probably not the most optimal

# Time: O(n)
# Space: O(n)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])