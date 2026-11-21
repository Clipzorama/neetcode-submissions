# Create a hash set and add all starting cities (the first element of each path) to it.
# Iterate through all paths and check each destination city (the second element).
# If a destination city is not found in the hash set, return it as the answer.

# time: O(n)
# space: O(n)

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        mp = {p[0]: p[1] for p in paths}

        start = paths[0][0]

        # ["Cedar","Oak"],["Maple","Cedar"]] --> prime example

        # you can see that "Oak" is not a key so it gets returned, unlike "Cedar"
        while start in mp:
            start = mp[start]
        
        return start
