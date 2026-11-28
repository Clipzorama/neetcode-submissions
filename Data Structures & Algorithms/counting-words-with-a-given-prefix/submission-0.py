class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        N = len(pref)

        for word in words:
            if word[:N] == pref:
                count += 1
        
        return count