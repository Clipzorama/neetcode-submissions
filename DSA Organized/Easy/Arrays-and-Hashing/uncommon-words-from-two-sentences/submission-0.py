from collections import Counter

# time: O(n + m)
# space: O(n + m)

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count = {}
        res = []

        # two seperate for loops but they increase in memory depending on the size of input
        # for both the array and hash table
        for w in s1.split(" ") + s2.split(" "):
            count[w] = count.get(w, 0) + 1
        
        for key, value in count.items():
            if value == 1:
                res.append(key)
        
        return res
                
        



            

