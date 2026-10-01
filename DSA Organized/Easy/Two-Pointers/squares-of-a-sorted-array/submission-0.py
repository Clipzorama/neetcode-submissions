class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # first we can square everything inside of the array

        s = list(map(lambda x: x**2, nums))
        res = []

        left = 0
        right = len(s) - 1

        while left <= right:
            if s[left] >= s[right]:
                res.append(s[left])
                left += 1
            else:
                res.append(s[right])
                right -= 1

        return res[::-1]