# time: O(n + m)
# space: O(n + m)

# the only difference is that this solution takes a list instead of a string so a new list dont have
# to be made every single time since list are mutable


# string immutability: when a string object is created in memory, it cannot be modified directly 
# and it would require a new string object in memory to modify it

# s = "hello"
# s[0] = "H"  ----> this wouldnt work since strings are immuatable

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        res = []

        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1
        
        while i < len(word1):
            res.append(word1[i])
            i += 1
        
        while j < len(word2):
            res.append(word2[j])
            j += 1
        
        return "".join(res)