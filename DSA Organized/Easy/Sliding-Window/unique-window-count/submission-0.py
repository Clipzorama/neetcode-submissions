from typing import List

# Given an array and k, count how many windows of size k contain only unique elements.

# time: O(n)
# space: O(n)

# beauitful sliding window solution
def problem(nums: List[int], k: int) -> int:
    count = 0
    hashmap = {}

    # establishing the first window
    for i in range(k):
        hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1

    # checking if there is any unique elements
    if len(hashmap) == k:
        count += 1


    for right in range(k, len(nums)):
        left = right - k

        hashmap[nums[left]] -= 1
        if hashmap[nums[left]] == 0:
            del hashmap[nums[left]]

        hashmap[nums[right]] = hashmap.get(nums[right], 0) + 1

        if len(hashmap) == k:
            count += 1


    return count
    


n = [1, 2, 3, 2, 4]
k = 3

# Output:
# 2

print(problem(n, k))