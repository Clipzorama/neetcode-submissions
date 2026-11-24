from collections import Counter

# time: O(n)
# Solution: O(1)

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        k = len(p)
        hashmap = {}
        theP = Counter(p)
        left = 0

        # doing the initial check first
        if k > len(s):
            return []
        
        for i in range(k):
            hashmap[s[i]] = hashmap.get(s[i], 0) + 1
        
        if hashmap == theP:
            res.append(0)
        
        for right in range(k, len(s)):
            hashmap[s[left]] -= 1

            if hashmap[s[left]] == 0:
                del hashmap[s[left]]
            
            left += 1

            hashmap[s[right]] = hashmap.get(s[right], 0) + 1

            # here we're appending the beginning of the next window so we add the value of 'left'
            # inside of the array

            if hashmap == theP:
                res.append(left)
        
        return res
            

        


