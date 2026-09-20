# also optimal but more SIMPLY WRITTEN
# time: O(n)
# space: O(n)

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for char in s:
            # If the current character is the opposite case of the last character, remove the pair
            # thats why swapcase is top tier
            if stack and stack[-1].swapcase() == char:
                stack.pop()

            # Otherwise, keep the current character
            else:
                stack.append(char)

        return "".join(stack)



result = Solution()
ss = "leEeetcode"
sss = "mC"
ssss = "kkdsFuqUfSDKK"
print(result.makeGood(ssss))