class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        # Time: O(n) - Each element is visited at most twice (left and right pointers).
        # Space: O(1) - Hashmap stores at most 3 distinct fruit types.

        hashmap = {}
        left = 0
        res = 0

        for right in range(len(fruits)):
            # Expand window and update fruit frequency
            hashmap[fruits[right]] = hashmap.get(fruits[right], 0) + 1

            # Shrink window when more than 2 distinct fruit types
            while len(hashmap) > 2:
                hashmap[fruits[left]] -= 1

                # Remove fruit type when its frequency reaches zero
                if hashmap[fruits[left]] == 0:
                    del hashmap[fruits[left]]

                left += 1

            # Update maximum valid window length --> can also add total instead of right - left + 1
            res = max(res, right - left + 1)

        return res