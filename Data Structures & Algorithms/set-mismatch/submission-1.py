# Time Complexity: O(n)
# Space Complexity: O(n)

# XOR = MISSING ^ DUPLICATE
# MISSING = XOR ^ DUPLICATE
# DUPLICATE = MISSING ^ XOR


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # to find missing number : xor ^ duplicate 

        seen = set()
        n = len(nums)
        xor = 0
        result = []

        # obtaining xor can be helpful in discovering the duplicate or missing number
        # you get xor, you can then calculate missing num, or duplicate depending on what value 
        # you know
        for i, num in enumerate(nums, start=1):
            xor ^= i
            xor ^= num

            # basically how we are finding the missing num
            if num in seen:
                duplicate = num

            seen.add(num)
        
        missing = xor ^ duplicate

        # then we append the results that we are looking for and then return the function --> BOOM
        result.append(duplicate)
        result.append(missing)

        return result


        