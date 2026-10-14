class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        hashmap = {}
        n = 1
        actualSum = 0
        n = len(grid) **2
        

        for i in range(len(grid)):

            for j in range(len(grid[i])):
                hashmap[grid[i][j]] = hashmap.get(grid[i][j], 0) + 1
                actualSum += grid[i][j]
        
        expectedSum = (n * (n+1)) // 2

        repeated = max(hashmap, key=hashmap.get)

        missing = expectedSum - actualSum + repeated


        return [repeated, missing]

