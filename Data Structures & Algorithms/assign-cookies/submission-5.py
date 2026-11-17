# Time: O(n log n + m log m)
# Space: O(1) or O(n + m) depending on the sorting algorithm

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        i = j = 0

        while i < len(g):
            
            # j increments if it doesnt align with the greed factor
            while j < len(s) and g[i] > s[j]:
                j += 1
            
            if j == len(s):
                break
            
            # i only increments when a greed factor is satisfied
            i += 1

            # j increments to the next cookie for the next available child who meet requirements
            j += 1
        
        return i 
