class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        # position where the next 0 shoulg go
        left = 0
        # current num we are checking
        curr = 0
        # position where the next two should go 
        right = len(nums) - 1

        while curr <= right:
            # then 
            if nums[curr] == 0:
                # Left side now has one more correctly placed 0
                nums[curr], nums[left] = nums[left], nums[curr]
                left += 1
                # from here we move to the next number
                curr += 1
            elif nums[curr] == 1:
                # 1 belongs in the middle so we move to next number
                curr += 1
            else:
                # Do NOT move curr because the swapped-in value must be checked
                nums[curr], nums[right] = nums[right], nums[curr]
                right -= 1

        print(nums)
                 
                 

result = Solution()
n = [2, 1, 0]
nn = [1,0,2]

print(result.sortColors(n))
print(result.sortColors(nn))

        

        