class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap = {}
        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word in hashmap:
                hashmap[sorted_word].append(word)
            else:
                hashmap[sorted_word] = [word]

        return list(hashmap.values())