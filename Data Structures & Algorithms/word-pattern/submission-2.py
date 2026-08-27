class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")

        if len(pattern) != len(words):
            return False

        # mapping the word to the pattern
        wordsToChar = {}

        # mapping the pattern to the word

        charToWord = {}

        # checking both dictionaries with zip and checking if there is a pattern

        '''
        zip() does the following:
        
            a dog
            b cat
            b cat
            a dog  

        ''' 

        for c, w in zip(pattern, words):
            if c in charToWord and charToWord[c] != w:
                return False
            if w in wordsToChar and wordsToChar[w] != c:
                return False

            #  "a": "dog"
            charToWord[c] = w

            #  "dog": "a"
            # and so on
            wordsToChar[w] = c

        return True