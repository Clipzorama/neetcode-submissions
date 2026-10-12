# time: O(n)
# space: O(n)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        hashmap = {}
        count = 0
        left = 0


        # iterating through the entire s and counting highest length as long as condition holds
        for right in range(len(s)):
            hashmap[s[right]] = 1 + hashmap.get(s[right], 0)

            highest = max(hashmap.values())

            # most important formula for the valid window meeting the condition

            while (right - left + 1) - highest > k:
                hashmap[s[left]] -= 1
                left += 1
            
            count = max(count, right - left + 1)
        
        return count
        