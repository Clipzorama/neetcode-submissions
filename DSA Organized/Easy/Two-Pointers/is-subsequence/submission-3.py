# did the solution again but its a bit different than the other one that i did 

# another two pointer solution  

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0
        right = 0
        # i have a variable counter to keep track but theres lots of ways to do it
        count = 0

        if len(s) == 0:
            return True

        while right < len(t):
            if s[left] == t[right]:
                count += 1
                left += 1
                right += 1

            else:
                right += 1

        return count == len(s)