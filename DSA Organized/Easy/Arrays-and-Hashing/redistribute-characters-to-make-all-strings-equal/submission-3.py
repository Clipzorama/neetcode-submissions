# Time Complexity: O(n * m) 

# Space Complexity: O(1)

class Solution:
    def makeEqual(self, words: List[str]) -> bool:

        hashmap = {}
        
        # gonna get all the frequencies from the list

        for word in words:
            for char in word:
                hashmap[char] = hashmap.get(char, 0) + 1
        
        # we need to know whether each character's total frequency can be divided evenly among those N 
        # words. MOST IMPORTANT PART OF SOLUTION
        
        for key in hashmap:
            # equivalent to (if hashmap[key] % len(words) != 0)
            if hashmap[key] % len(words):
                return False
        
        return True

        