class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0
        right = 0
        count = 0

        if len(s) == 0:
            return True

        while right < len(t) and left != len(s):
            if s[left] == t[right]:
                count += 1
                left += 1
                right += 1
            else:
                right += 1

        return count == len(s)