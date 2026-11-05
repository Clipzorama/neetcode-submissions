# so this is a circular array + sliding window solution

# Time: O(N)

# Space: O(1)

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        res = 0
        N = len(colors)
        l = 0

        # the number of windows wrt the sliding window constraints (k) and 
        # circular array logic

        for r in range(1, N + k - 1):
            
            # making sure that the values are not adjacently equal
            if colors[(r - 1) % N] == colors[r % N]:
                l = r
            
            # if window is too big, we shrink
            if r - l + 1 > k:
                l += 1
            
            # assuming window meets requirements
            if r - l + 1 == k:
                res += 1
        

        return res

            


