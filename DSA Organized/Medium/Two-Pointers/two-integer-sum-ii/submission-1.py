class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # sliding window approach?
        left = 0
        right = len(numbers) - 1
        result = 0

        while result < 1:

            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1

            elif numbers[left] + numbers[right] == target:
                result = 1


        return [left + 1, right + 1]