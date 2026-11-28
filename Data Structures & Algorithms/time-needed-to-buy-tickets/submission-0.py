# time: O(n * m)
# space: O(n)

# solution using deque --> very clever way to keep tabs on someone (in code LOL)

from collections import deque

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        d = deque()
        time = 0

        for i in range(len(tickets)):
            d.append(i)
        

        while tickets:
            time += 1
            cur = d.popleft()

            tickets[cur] -= 1

            # if the value of the index is 0, then we check if it is the same person as k
            # so we can stop the iteration and return time

            if tickets[cur] == 0:
                if cur == k:
                    return time
            else:
                d.append(cur)
        
        return Time

        