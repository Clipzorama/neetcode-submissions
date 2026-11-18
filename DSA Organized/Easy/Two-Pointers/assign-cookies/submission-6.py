class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        # first we are going to sort g and s so we can check everything in order

        g.sort()
        s.sort()

        i = j = 0

        while i < len(g):

            while j < len(s) and g[i] > s[j]:
                j += 1
            
            if len(s) == j:
                break

            i += 1
            j += 1


        return i
