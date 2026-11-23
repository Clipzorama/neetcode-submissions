# solution when you're using a stack

# time: O(n)
# space: O(n)

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for log in logs:

            if log == "./":
                continue
            
            if stack and log == "../":
                stack.pop()
            elif len(stack) == 0 and log == "../":
                continue
            else:
                stack.append(log)
            
        return len(stack)