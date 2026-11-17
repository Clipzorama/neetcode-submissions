from typing import List

def findContentChildren(g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        write = 0
        count = 0

        for read in range(len(g)):
            if g[read] <= s[write]:
                count += 1
            
                if write < len(s) - 1:
                    write += 1
                else:
                    break
        
        return count

gg=[10,9,8,7]
ss=[5,6,7,8]

print(findContentChildren(gg, ss))