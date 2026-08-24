class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pusher = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[pusher] = nums[i]
                pusher += 1
        
        return len(nums[:pusher])

        