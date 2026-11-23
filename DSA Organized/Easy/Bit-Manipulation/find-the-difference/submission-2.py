from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        ss = Counter(s)
        tt = Counter(t)

        for key, value in tt.items():
            if value != ss[key]:
                return key