class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        hashmap2 = {}

        for i in range(len(s)):
            hashmap[s[i]] = hashmap.get(s[i], 0) + 1

        for j in range(len(t)):
            hashmap2[t[j]] = hashmap2.get(t[j], 0) + 1

        return hashmap == hashmap2