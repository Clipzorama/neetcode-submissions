# Time: O(n log n + m log m)
# Space: O(1) or O(n + m) depending on the sorting algorithm


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        # first we are going to sort g and s so we can check everything in order

        g.sort()
        s.sort()

        i = j = 0

        # i must be less than g as we're checking all of the children 
        while i < len(g):

            while j < len(s) and g[i] > s[j]:
                j += 1
            
            if len(s) == j:
                break

            # if a child is satified, then we can increment i
            i += 1
            j += 1


        # we're returning where i left off
        return i
