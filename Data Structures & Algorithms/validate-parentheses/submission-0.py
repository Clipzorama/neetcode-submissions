class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeP = {")": "(", "]": "[", "}": "{"}

        # iterate the entire s
        for c in s:
            # check if char in a closing string. if so, if/else is executed
            if c in closeP:
                if stack and stack[-1] == closeP[c]:
                    stack.pop()
                else:
                    return False

            # if opening parenthesis, then element is appending into the stack
            else:
                stack.append(c)

        if len(stack) > 0:
            return False

        return True
        