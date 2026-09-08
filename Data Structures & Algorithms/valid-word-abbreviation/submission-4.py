class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # pointer for word
        p1 = 0 
        # pointer for abbr
        p2 = 0 

        while p1 < len(word) and p2 < len(abbr):

            # Case 1: abbreviation has a letter
            if abbr[p2].isalpha():
                if word[p1] != abbr[p2]:
                    return False

                p1 += 1
                p2 += 1

            # Case 2: abbreviation has a number
            elif abbr[p2].isdigit():

                if abbr[p2] == "0":
                    return False

                num = 0
                # build the full number
                while p2 < len(abbr) and abbr[p2].isdigit():
                    # a way to build full numbers from digit strings "18" --> 18 (int) instead of "1" and "8"
                    num = num * 10 + int(abbr[p2])
                    p2 += 1

                # skipping the numbers in word
                p1 += num

            else:
                return False


        return p1 == len(word) and p2 == len(abbr)