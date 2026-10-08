from typing import List

# time: O(n)
# space: O(1)


'''

Assume all numbers are positive...

Given nums and k, return the length of the longest contiguous subarray whose sum is less than or equal to k.

'''

def problem(nums: List[int], k: int) -> int:
    currSum = 0
    maxLength = float("-inf")
    currLength = 0
    left = 0

    for right in range(len(nums)):
        currSum += nums[right]

        while currSum > k:
            currSum -= nums[left]
            left += 1

        currLength = right - left + 1
        maxLength = max(maxLength, currLength)


    if maxLength == float("-inf"): return 0

    return maxLength

n = [1, 2, 1, 1, 1, 3]
kk = 4
print(problem(n, kk))