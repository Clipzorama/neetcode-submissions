# Time: O(n) --> s.count("1") traverses the string once,
#                 and the for loop traverses it once more.


# Space: O(1) --> Only three integer variables are used
#                  (ones, zeros, maxScore).
#                  Updating their values doesn't require
#                  additional memory proportional to n.


class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count("1")
        zeros = 0
        maxScore = 0

        # excluding the last character because we want to keep a string on the right side 
        # Since we're splitting of course
        for i in range(len(s) - 1):
            if s[i] == "0":
                zeros += 1
            else:
                ones -= 1
            
            maxScore = max(maxScore, ones + zeros)
        
        return maxScore