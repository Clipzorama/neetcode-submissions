# time: O(n)
# space: O(n)


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        count = 0
        left = 0

        for right in range(len(s)):
            hashmap[s[right]] = hashmap.get(s[right], 0) + 1
            
            # we're getting the most frequent characters here
            highest = max(hashmap.values())

            # this would make the window invalid as we only have k replacements
            while (right - left + 1) - highest > k:
                hashmap[s[left]] -= 1
                left += 1
            
            # count records the length that best fits the window of consecutive characters
            count = max(count, right - left + 1)
        
        return count