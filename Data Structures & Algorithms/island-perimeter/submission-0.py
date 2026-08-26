class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set()

        # We will need to use Depth-First-Search for this problem

        def dfs(i, j):
            perimeter = 0

            # i >= len(grid) or j >= len(grid[i]) --> implies that the row or column is out of bounds and most 
            # return 1 since we will be counting 1 to the edge
            # Basically a condition for an index out of range to return a one
            if i >= len(grid) or j >= len(grid[i]) or i < 0 or j < 0 or grid[i][j] == 0:
                return 1

            # Both are base cases for the recursion

            if (i, j) in visit:
                return 0

            # adding the coordinates as a tuple inside of the visit set.

            visit.add((i, j))

            # adding to the perimeter within each direction.
            perimeter += dfs(i, j + 1)
            perimeter += dfs(i, j - 1)
            perimeter += dfs(i + 1, j)
            perimeter += dfs(i - 1, j)
            return perimeter


        # we iterate through each element in each nested list. if element is present somewhere we execute dfs
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    return dfs(i, j)