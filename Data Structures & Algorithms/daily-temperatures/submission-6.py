# time: O(n)
# space: O(n)

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        result = [0] * len(temperatures)

        # Monotonic decreasing stack: store [temperature, index] for unresolved days.
        stack = []

        for idx, t in enumerate(temperatures):

            # Current temperature resolves all colder temperatures waiting on the stack.
            while stack and t > stack[-1][0]:

                stackT, stackIdx = stack.pop()

                # Difference between current warmer day and the previous colder day.
                result[stackIdx] = idx - stackIdx

            # This day now waits for a future warmer temperature.
            stack.append([t, idx])

        # Anything left in the stack has no warmer future day, so it stays 0.
        return result


# result = Solution()
# t = [34,80,80,80,34,80,80,80,34,34]
# ttt = [55,38,53,81,61,93,97,32,43,78]
# print(result.dailyTemperatures(t))
# print(result.dailyTemperatures(ttt))


# [1,4,1,2,1,0,0]
