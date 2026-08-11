class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0

        # This is a two pointer solution but the time complexity is still O(m + n)
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)