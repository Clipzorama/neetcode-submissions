class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []

        for op in operations:
            if op.lstrip("-").isdigit():
                res.append(int(op))
            elif op == "+" and len(res) > 1:
                res.append(int(res[-1]) + int(res[-2]))
            elif op == "C":
                res.pop()
            elif op == "D":
                res.append(res[-1] * 2)



        return sum(res)
        