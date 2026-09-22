# doing this solution again to understand the pattern

# time: O(n)
# space: O(n)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for idx, t in enumerate(temperatures):
            
            # while loop iterates over it more than once just in case theres multiple conditions
            while stack and t > stack[-1][0]:
                stackT, stackIdx = stack.pop()
                result[stackIdx] = idx - stackIdx
            
            stack.append([t, idx])
        
        return result