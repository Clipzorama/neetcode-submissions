# Time: O(n log n) because of sorting.
# Space: typically O(1)

class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        # Sort people by weight so we can use two pointers
        people.sort()

        # Count the number of boats needed
        boat = 0

        # Left points to the lightest person, right to the heaviest
        l, r = 0, len(people) - 1

        # Continue until every person has been placed in a boat
        while l <= r:
            # If the lightest and heaviest cannot fit together, the heaviest goes alone
            if people[l] + people[r] > limit:
                r -= 1
                boat += 1

            # Otherwise, pair the lightest and heaviest together
            else:
                l += 1
                r -= 1
                boat += 1

        return boat