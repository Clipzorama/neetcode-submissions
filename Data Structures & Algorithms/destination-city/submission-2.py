# time: O(n)
# space: O(n)

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s = set()

        # this one works as well because it gets all the cities despite the destination city
        for p in paths:
            s.add(p[0])
        
        for p in paths:
            if p[1] not in s:
                return p[1]
