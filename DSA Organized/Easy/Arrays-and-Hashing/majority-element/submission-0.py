class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target = len(nums) // 2
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        for key, value in hashmap.items():
            if value > target:
                return key

        return 0