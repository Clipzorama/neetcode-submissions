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