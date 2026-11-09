# we'll do this question again for practice on sliding windows and with this specific type of problem

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # to record all of the frequencies
        hashmap = {}

        # how we will record the highest
        count = 0

        # this is how we will slide the window
        left = 0

        for right in range(len(s)):
            hashmap[s[right]] = hashmap.get(s[right], 0) + 1

        
            highest = max(hashmap.values())

            while (right - left + 1) - highest > k:
                hashmap[s[left]] -= 1
                left += 1

            count = max(count, right - left + 1)
        

        return count

        