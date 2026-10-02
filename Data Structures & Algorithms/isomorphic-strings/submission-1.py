# time: O(n)
# space: O(n) - worst case if the characters can be arbitrary and all distinct, the maps can grow with n

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapS, mapT = {}, {}

        for i in range(len(s)):

            # getting values inside of both parameters (both the same size)
            c1, c2 = s[i], t[i]

            # a condition to check if the same character is about to be mapped to another character
            # if so, both strings wouldnt be isomorphic

            # like o being mapped a and then seeing that o doesnt equal r...
            if (c1 in mapS and mapS[c1] != c2 or c2 in mapT and mapT[c2] != c1):
                return False


            # here we wuld be mapping each char with a distinct character
            mapS[c1] = c2   
            mapT[c2] = c1
        
        return True
       
'''

Input: s = "foo", t = "bar"

Output: false

'''
        