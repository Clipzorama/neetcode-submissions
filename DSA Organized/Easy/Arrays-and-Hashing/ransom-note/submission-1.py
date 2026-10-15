from collections import Counter

# TIME COMPLEXITY: O(n + m)
# - n = len(ransomNote), m = len(magazine).
# - Counter counts character frequencies in both strings.
# - Comparing frequencies takes O(1) per unique character.
# - Overall time complexity is O(n + m).

# SPACE COMPLEXITY: O(1)
# - Two dictionaries store character frequencies.
# - Each stores at most 26 lowercase English letters.
# - Therefore, auxiliary space is O(1).

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = dict(Counter(ransomNote))
        mag = dict(Counter(magazine))


        # iterates by key inside of the hashmap
        for char in ransom:
            
            # if char is not in mag then obv False
            if char not in mag:
                return False
            
            # if frequency is higher in ransom than mag than we know it cant be constructed
            if ransom[char] > mag[char]:
                return False
        
        return True
