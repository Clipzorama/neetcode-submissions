# this solution is much more simpler yet space complexity is higher:

# time: O(n)
# space: O(n) --> since the stack adds elements depending on the size of the input

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        # stack removes elements from the end everytime "#" is encountered
        def build(text):
            stack = []
            for char in text:
                if char == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            # we return the stack 
            return stack
        
        # Comparing the two lists works perfectly, so you do not need to convert them back into strings.
        return build(s) == build(t)
