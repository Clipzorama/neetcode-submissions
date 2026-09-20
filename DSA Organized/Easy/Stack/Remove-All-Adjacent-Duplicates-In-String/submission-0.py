# time: O(n) 
# space: O(n) --> since iterable is appending valid elements in respect to input size 

class Solution:
    def removeDuplicates(self, s: str) -> str:

        # only removing elements that have adjacent duplicates!
        stack = []

        for char in s:
            # If the current character matches the most recent
            # unmatched character, remove the previous one
            if stack and stack[-1] == char:
                stack.pop()
            else:
                # append if there is no adjacent duplicates
                stack.append(char)

        # add back into a string
        return "".join(stack)

        



result = Solution()
ss = "abbaca" # "ca"
print(result.removeDuplicates(ss))