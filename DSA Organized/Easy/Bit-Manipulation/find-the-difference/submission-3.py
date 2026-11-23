
# time: O(n)
# space: O(1)

# i am gonna try another solution that uses bit manipulation.
# something that is asymptotically optimal!

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        

        # this solution takes O(1) auxiliary space which is so much better
        res = 0

        for char in s:
            res ^= ord(char)
        
        for char in t:
            res ^= ord(char)
        
        # the different "num" will be translated into its ASCII letter!
        return chr(res)
        