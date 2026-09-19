class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while l < r:
            cur = numbers[l] + numbers[r]

            if cur > target:
                r -= 1
            elif cur < target:
                l += 1
            elif cur == target:
                return [l+1, r+1]
        
        return -1