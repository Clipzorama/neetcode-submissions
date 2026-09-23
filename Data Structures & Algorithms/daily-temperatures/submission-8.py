class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for idx, t in enumerate(temperatures):

            while stack and stack[-1][0] < t:
                stackT, stackIdx = stack.pop()
                result[stackIdx] = idx - stackIdx
            
            stack.append([t, idx])
        
        return result