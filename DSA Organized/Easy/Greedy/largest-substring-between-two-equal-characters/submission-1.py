# time: O(n) --> one for loop
# space: O(1) --> since there is 26 different characters in the alphabet (all lowercase)

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # we can capture the char and index and if the char pops up again, then we return the value
        # we check to see if that is the highest

        hashmap = {}

        # if condition is never true, we just return -1
        res = -1
        
        for i, char in enumerate(s):
            # if word is in dictionary then we already came across it so we can substract the 
            # indexes together
            if char in hashmap:
                res = max(res, i - hashmap[char] - 1)
            else:
                hashmap[char] = i
        
        return res