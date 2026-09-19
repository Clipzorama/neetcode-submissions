# optimal solution

# time: O(n log n) + O(n²) --> O(n²)
# space: O(1) --> excluding output array

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # adding a list and sorting the array
        res = []
        nums.sort()

        # to prevent finding same triplets and promoting uniqueness.
        # we already found all combinations with -1, we dont need to do it again, so we skip to next unique element

        for i, a in enumerate(nums):
            if i > 0 and nums[i - 1] == a:
                continue

            l, r = i + 1, len(nums)-1

            # implementing two sum II
            while l < r:
                thresSum = a + nums[l] + nums[r]
                if thresSum > 0:
                    r -= 1
                elif thresSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    # after finding one solution we HAVE to increment to continue or else itll be infinite
                    l += 1

                    # to make sure the problem gets unique triplets instead of the same thing
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res





n = [-1,0,1,2,-1,-4]
result = Solution()
print(result.threeSum(n))