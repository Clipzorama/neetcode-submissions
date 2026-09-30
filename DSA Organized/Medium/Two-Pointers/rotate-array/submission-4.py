from collections import deque

# not the most optimal but it works really well

# Time:  O(n)
# Space: O(n)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        d = deque()
        left = 0
        right = len(nums) - 1

        # calculates the number of rotations even if k > len(nums)
        k %= len(nums)
        
        # our limit to extract from
        split = len(nums) - k

        # extracting the last k elements and appending left
        while right >= split:
            d.appendleft(nums[right])
            right -= 1
        
        # extracting the first k - 1 elements
        while left < split:
            d.append(nums[left])
            left += 1
        
        # convert deque into list and then place with nums list
        result = list(d)
        nums[:] = result


    
        



        