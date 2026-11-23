# something a bit more optimal in terms of space complexity

# time: O(n)
# space: O(1)

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0

        for log in logs:
            if log == "./":
                continue
            
            elif log == "../":

                if depth > 0:
                    depth -= 1
                else:
                    depth = 0   

            else:
                depth += 1
        
        return depth
        