
class Solution:
    def makeEqual(self, words: List[str]) -> bool:

        hashmap = {}
        
        # gonna get all the frequencies from the list

        for word in words:
            for char in word:
                hashmap[char] = hashmap.get(char, 0) + 1
        
        for key in hashmap:
            if hashmap[key] % len(words):
                return False
        
        return True

        