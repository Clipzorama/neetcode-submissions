'''
OPTIMAL SOLUTION:

Time: O(n)
Space: O(n)


# Floor always goes down toward negative infinity.

# Truncation always goes toward zero.

# thats why we add int() here instead of floor division //

Positive numbers look the same : 
int(2.8)   # 2
2.8 // 1   # 2

BUT NOT for negative numbers

int(-2.8)   # -2   ← toward 0
-2.8 // 1   # -3   ← toward negative infinity (which we dont want in this solution)


'''

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for t in tokens:
            # we want to count negative numbers as well so we keep this too!
            if t.lstrip("-").isdigit():
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()

                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                else:
                    # int implementation instead of floor division
                    stack.append(int(a / b))

        return stack[0]


# t = ["1","2","+","3","*","4","-"]
tt=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

result = Solution()
# print(result.evalRPN(t))
print(result.evalRPN(tt))

        