class Solution:
    def maxDifference(self, s: str) -> int:
        hashmap = {}
        maxD = float("-inf")

        for char in s:
            hashmap[char] = 1 + hashmap.get(char, 0)
        
        for odd in hashmap.values():
            if odd % 2 == 0:
                continue
            for even in hashmap.values():
                if even % 2 != 0:
                    continue 
                maxD = max(maxD, odd - even)
        
        return maxD

        