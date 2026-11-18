# time: O(n * m)
# space: O(1)

# n = number of words in words.
# m = maximum length of a word.
# k = number of characters in allowed.

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        # we start with a total of all the words
        total = len(words)


        # puts each char inside of the set 
        a = set(allowed)

        for word in words:

            for char in word:
                
                # if a char is not inside of the set, then we remove that letter from the 
                # total and continue to the next word hence, break
                if char not in a:
                    total -= 1
                    break
        
        # we return what is left
        return total