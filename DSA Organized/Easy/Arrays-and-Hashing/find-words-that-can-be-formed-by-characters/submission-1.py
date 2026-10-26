
# if you want to use collections
from collections import Counter

# Time: O(n + (m * k))
# Space: O(1) since there is a max of 26 letters inside of the alphabet (only lowercase)

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)
        res = 0

        # for each word, we get its frequency
        for w in words:
            wordle = Counter(w)
            flag = True
            

            # checking to see if the frequency is greater than what is needed make the 
            # word from 'chars'
            for char in wordle:
                if wordle[char] > count[char]:
                    flag = False
                    break
            
            if flag:
                res += len(w)
            else:
                continue
        

        return res
                    