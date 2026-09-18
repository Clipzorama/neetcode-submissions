# This is a STACK PATTERN!!!!

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for char in s:

            # this if-statement checks if the element in iteration is a closed parenthesis or not 
            if char in pairs:

                # checking if the stack is empty or the last element contains a closing 
                # value first

                if not stack or stack[-1] != pairs[char]:
                    return False

                # either way after checking we pop it out and check whats valid next
                stack.pop()
            
            else:
                # if its not in pairs then we know it must be an opening parenthesis
                stack.append(char)

        # we check if the stack is empty, if so then every opening parenthesis has a closed 
        # one
        return len(stack) == 0