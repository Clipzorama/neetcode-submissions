class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mini = min(strs, key=len)
        res = ""

        for i in range(len(mini)):

            for char in strs:
                if char[i] != mini[i]:
                    return res
                
            res += mini[i]
        

        return res