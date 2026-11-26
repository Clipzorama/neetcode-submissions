# time: O(n)
# space: O(1)

class Solution:
    def romanToInt(self, s: str) -> int:
        
        # Map each Roman numeral to its corresponding integer value
        roman = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100, "D": 500, "M": 1000
        }

        # Initialize the variable that stores the total integer value
        res = 0

        # Iterate through each character in the Roman numeral string
        for i in range(len(s)):

            # Check if the next character exists and has a greater value than the current character
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:

                # Subtract the current value because a smaller numeral precedes a larger numeral
                res -= roman[s[i]]

            # Otherwise, the current numeral should be added
            else:

                # Add the current Roman numeral's integer value to the result
                res += roman[s[i]]

        # Return the final converted integer
        return res

        