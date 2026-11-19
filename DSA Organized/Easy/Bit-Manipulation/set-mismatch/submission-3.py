from collections import Counter

class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        count = Counter(nums)
        res = [0, 1] # [duplicate, missing]


        # We're iterating through the expected values (1 through n), not the indices of the list.
        # so we're looking at the keys rather than anything else
        for i in range(1, n + 1):

            # its clear to know whats missing (perks of using Counter)
            # doesnt submit a key error, if a key is not present, but instead adds a 0 in its value 
            # for that key
            if count[i] == 0:
                res[1] = i
            
            # clear that this would be the duplicate number
            elif count[i] == 2:
                res[0] = i
        
        return res