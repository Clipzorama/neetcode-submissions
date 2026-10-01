# time: O(n)
# space: O(n)

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # first we can square everything inside of the array
        s = list(map(lambda x: x**2, nums))

        res = []
        
        # initialize our two pointers
        left = 0
        right = len(s) - 1

        # we make a while loop and compared the values on both sides to get the descending order list
        while left <= right:
            if s[left] >= s[right]:
                res.append(s[left])
                left += 1
            else:
                res.append(s[right])
                right -= 1

        # we return the reversed solution as it will be in ascending order
        return res[::-1]