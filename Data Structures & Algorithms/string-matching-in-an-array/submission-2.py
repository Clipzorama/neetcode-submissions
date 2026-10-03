# most standard approach is this one and it is:

# time: O(n)^2
# space: O(1)


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        result = set()

        i = 0
        j = 1

        while i < len(words) - 1:

            if j == len(words):
                i += 1
                j = i + 1

                # the continue keyword rechecks the while condition
                continue 
            
            if words[i] in words[j]:
                result.add(words[i])
            
            elif words[j] in words[i]:
                result.add(words[j])
            
            j += 1
        

        return list(result)