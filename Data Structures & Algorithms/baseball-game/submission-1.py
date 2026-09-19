# very simple solution just like the previous one

# time: O(n)
# space: O(n)

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []

        # making sure there is two elements inside res that can be added 
        for op in operations:
            if op == "+" and len(res) > 1:
                res.append(res[-1] + res[-2])
                
            # everything is self-explanatory
            elif op == "C":
                res.pop()
            elif op == "D":
                res.append(res[-1] * 2)
            else:
                # instead of doing String.lstrip("-")
                res.append(int(op))
        
        return sum(res)