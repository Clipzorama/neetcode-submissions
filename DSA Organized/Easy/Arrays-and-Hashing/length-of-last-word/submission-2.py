# more optimal approach for this problem

# Time: O(n) in the worst case.

# Space: O(1) because you're only using i and length, without creating another list like split() does.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        length = 0

        # keep decrementing until we reach a letter
        while s[i] == " ":
            i -= 1
        
        # the second we reach a word, we count how much characters are inside of it 
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        
        # return the first letter length we come across from the end!
        return length


        