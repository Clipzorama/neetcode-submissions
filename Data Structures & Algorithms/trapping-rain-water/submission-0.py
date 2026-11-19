# time: O(n)
# space: O(1)

class Solution:
    def trap(self, height: list[int]) -> int:
        lmax, rmax, water = 0, 0, 0
        l, r = 0, len(height) - 1

        while l <= r:
            
            # this is the easy and simple calculation to calculate the trapped rain water

            if lmax <= rmax:
                lmax = max(lmax, height[l])
                water += lmax - height[l]
                l += 1

            # condition if rightside wall is smaller than left side
            else:
                rmax = max(rmax, height[r])
                water += rmax - height[r]
                r -= 1
        
        return water
        