
# time: O(n + m)
# space: O(n + m)


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        # best way, is to concatenate the strings together

        return "".join(word1) == "".join(word2)

