class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        # Go through each value once.
        for i, num in enumerate(nums):

            # Instead of searching for another number blindly,
            # calculate EXACTLY what number we need.
            complement = target - num

            # Ask:
            # "Have I already seen the number that completes the pair?"
            if complement in hashmap:

                # hashmap stores:
                # number -> its index
                return [hashmap[complement], i]

            # If we haven't found a pair yet,
            # remember this number for future elements.
            hashmap[num] = i