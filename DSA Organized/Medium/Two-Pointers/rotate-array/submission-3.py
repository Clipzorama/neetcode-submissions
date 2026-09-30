from collections import deque

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    
        d = deque()

        left = 0
        k %= len(nums)

        right = len(nums) - 1
        split = len(nums) - k

        while right >= split:
            d.appendleft(nums[right])
            right -= 1
        
        while left < split:
            d.append(nums[left])
            left += 1

        result = list(d)
        nums[:] = result



        