# Time: O(n)
# Space: O(1)

# Very simple solution

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        

        # this checks the first condition becfore confirming with the second condition
        for i in range(len(sentence)):
            if sentence[i] == " " and sentence[i-1] != sentence[i+1]:
                return False
        

        # instead of using split method, can just return the first and last index and check
        # if theyre equal or not
        if sentence[-1] != sentence[0]:
            return False

        return True 
