
# if you want to use collections
from collections import Counter

# Time: O(n + m)

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)
        res = 0

        for w in words:
            wordle = Counter(w)
            flag = True

            for char in wordle:
                if wordle[char] > count[char]:
                    flag = False
                    break
            
            if flag:
                res += len(w)
            else:
                continue
        

        return res
                    