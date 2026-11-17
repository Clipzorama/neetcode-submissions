from collections import Counter

# time O(n)
# space: O(n)

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # this algorithm basically check if there isn't a valid pair present.
        d = Counter(nums)

        for value in d.values():
            # if not then this resorts to a false conclusion
            if value % 2 == 1:
                return False
        
        return True
        