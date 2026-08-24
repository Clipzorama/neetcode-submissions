class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            # 5#Hello5#World --> Example
            res += str(len(word)) + "#" + word
        
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            # length is the number that is from the encode but coverted to int
            length = int(s[i:j])
            # slicing from the first letter in word after # to the end of the word    
            # (exclusive)

            res.append(s[j + 1: j + 1 + length])

            # Continues to the next word
            i = j + 1 + length
        
        return res
