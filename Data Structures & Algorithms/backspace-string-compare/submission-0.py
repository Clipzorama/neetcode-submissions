# this solution is much more simpler yet space complexity is higher:

# time: O(n)
# space: O(n) --> since the stack adds elements depending on the size of the input

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        # lets make a function to then call for the return value of this

        def build(text):
            stack = []

            for char in text:
                
                # the condition if we come across a hashtag
                if char == "#":

                    # we pop the recent word and go on to the iteration if stack is not empty
                    if len(stack) > 0:
                        stack.pop()
                    else:
                        continue
                else:
                    stack.append(char)
            
            return "".join(stack)
        

        # after completion, we check both texts if they're equal or not after modification
        return build(s) == build(t)
