# Brute Force Solution with Two Pointer
'''

Time complexity: O(n²) because for each i, the inner j loop can scan most of the remaining array.

Space complexity: O(1) because you only use a fixed number of variables (minimum, counter, changes, i, j) regardless of the input size.

'''

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minimum = 1000

        # nested for loop
        for i in range(len(blocks)):
            counter = 0
            changes = 0

            if blocks[i] == "W":
                changes += 1
                counter += 1
            elif blocks[i] == "B":
                counter += 1
            
            if counter == k:
                minimum = min(minimum, changes)

            for j in range(i + 1, len(blocks)):
                if blocks[j] == "W":
                    changes += 1
                    counter += 1
                elif blocks[j] == "B":
                    counter += 1


                if counter == k:
                    minimum = min(minimum, changes)

        return minimum 