from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:

        hashmap = Counter(s)

        for i, char in enumerate(s):
            if hashmap[char] == 1:
                return i
        
        return -1
        