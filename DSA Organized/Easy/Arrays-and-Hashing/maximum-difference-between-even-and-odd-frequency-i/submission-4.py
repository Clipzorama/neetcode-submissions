class Solution:
    def maxDifference(self, s: str) -> int:
        hashmap = {}

        
        maxEven = float("inf")
        maxOdd = float("-inf")

        for char in s:
            hashmap[char] = 1 + hashmap.get(char, 0)
        
        for count in hashmap.values():
            if count % 2 == 0:
                maxEven = min(maxEven, count)
            else:
                maxOdd = max(maxOdd, count)
        
        return maxOdd - maxEven
