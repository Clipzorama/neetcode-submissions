# this is a optimal solution yet, a bit more complicated than it has to be

# time: O(n)
# space: O(n)


class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for char in s:
           # Both characters are the same uppercase letter, so keep the current character
            if stack and stack[-1].isupper() and char.isupper() and char == stack[-1]:
                stack.append(char)

            # Current character is uppercase and matches the previous lowercase letter
            elif stack and char.isupper() and char == stack[-1].upper():
                stack.pop()

            # Previous character is uppercase and matches the current lowercase letter
            elif stack and stack[-1].isupper() and char.upper() == stack[-1]:
                stack.pop()

            # No matching opposite-case pair, so keep the current character
            else:
                stack.append(char)

        # overall we return it as a string
        return "".join(stack)

