# Time Complexity: O(n)
# - We traverse s2 once using a fixed-size sliding window.
# - Dictionary comparisons are O(1) since there are at most 26 lowercase letters.
# - Therefore, each window takes O(1) work, making the overall complexity O(n).

# Space Complexity: O(1)
# - Both hashmaps store at most 26 unique characters.
# - Space remains constant regardless of input size.

from collections import Counter

# since at most there is 26 letters (all lowercase) solution is o(n) time , O(1) space
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        k = len(s1)
        target = Counter(s1)
        hashmap = {}
        left = 0

        # getting the first k size window to check comparison. 
        for i in range(k):
            hashmap[s2[i]] = hashmap.get(s2[i], 0) + 1
        
        # checking the first condition
        if hashmap == target:
            return True


        # then after, we delete from the left and increase from the right side to check if 
        # both hashmaps are equal

        for right in range(k, len(s2)):
            hashmap[s2[left]] -= 1
            if hashmap[s2[left]] == 0:
                del hashmap[s2[left]]
            left += 1
            hashmap[s2[right]] = 1 + hashmap.get(s2[right], 0)
            if hashmap == target:
                return True
        
        return False
        

        