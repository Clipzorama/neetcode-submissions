from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        k = len(s1)
        target = Counter(s1)
        hashmap = {}
        left = 0

        for i in range(k):
            hashmap[s2[i]] = hashmap.get(s2[i], 0) + 1
        
        if hashmap == target:
            return True


        for right in range(k, len(s2)):
            hashmap[s2[left]] -= 1
            if hashmap[s2[left]] == 0:
                del hashmap[s2[left]]
            left += 1
            hashmap[s2[right]] = 1 + hashmap.get(s2[right], 0)
            if hashmap == target:
                return True
        
        return False
        

        