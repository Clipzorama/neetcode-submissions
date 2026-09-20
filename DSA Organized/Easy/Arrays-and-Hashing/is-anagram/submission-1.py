from collections import Counter

# same solution but using collections module
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        text1 = Counter(s)
        text2= Counter(t)

        return text1 == text2
        