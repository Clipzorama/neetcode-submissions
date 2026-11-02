# can also do this solution without enumerate() and just with the monotonic stack


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):

            while stack and temperatures[stack[-1]] < temperatures[i]:
                prevIdx = stack.pop()

                res[prevIdx] = i - prevIdx
            
            stack.append(i)

        return res