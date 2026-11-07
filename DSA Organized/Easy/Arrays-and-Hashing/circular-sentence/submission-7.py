# Time: O(n)
# Space: O(1)

# Very simple solution

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:

        for i in range(len(sentence)):
            if sentence[i] == " " and sentence[i-1] != sentence[i+1]:
                return False
        
        if sentence[-1] != sentence[0]:
            return False

        return True 
