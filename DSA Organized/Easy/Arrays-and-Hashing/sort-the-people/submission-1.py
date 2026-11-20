# Time Complexity: O(n log n)

# Space Complexity: O(n)



class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hashmap = {}
        
        # first we are going to zip since itll be easier to sort everything

        # (height,name) = zip
        for h, n in zip(heights, names):
            hashmap[h] = n
        
        
        # then we add the list and then appended the heights connected names in reversed order
        result = []
        for h in reversed(sorted(heights)):
            result.append(hashmap[h])
        
        return result