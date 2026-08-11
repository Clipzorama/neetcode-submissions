class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        if len(s) == 1:
            return 0

        i = 1
        while i < len(s):
            total += abs(ord(s[i]) - ord(s[i-1]))
            i += 1

        return total
        