from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # original algorithm to see the amount of words you can form given what is available
        countedText = Counter(text)
        balloons = Counter("balloon")

        result = float("inf")

        # no matter what you get the min number from words you have in param and cross reference the word youre looking to check
        for c in balloons:
            result = min(result, countedText[c] // balloons[c])
        
        return result

        