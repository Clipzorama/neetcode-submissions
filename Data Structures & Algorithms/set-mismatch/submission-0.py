

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # to find missing number : xor ^ duplicate 

        seen = set()
        n = len(nums)
        xor = 0
        result = []

        for i, num in enumerate(nums, start=1):
            xor ^= i
            xor ^= num

            if num in seen:
                duplicate = num

            seen.add(num)
        
        missing = xor ^ duplicate

        result.append(duplicate)
        result.append(missing)

        return result


        