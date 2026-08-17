
# Time Complexity: O(log n) --> WHEN ARRAY IS ALREADY SORTED
# Time Complexity: O(n log n)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # every iteration were checking if the solution is the value of num[mid]
            if nums[mid] == target:
                return mid
            
            # then we check from mid -1 and wherever left is
            elif target < nums[mid]:
                right = mid - 1
            
            # then we check from mid +1 and wherever right is
            elif target > nums[mid]:
                left = mid + 1
        
        return -1