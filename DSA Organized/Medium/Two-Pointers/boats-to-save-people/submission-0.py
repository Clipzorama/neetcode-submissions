class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        # this way it would be easier to point and go from there
        people.sort()

        boat = 0

        l, r = 0, len(people) - 1

        while l <= r:
            if people[l] == limit:
                boat += 1
                l += 1
            elif people[r] == limit:
                boat += 1
                r -= 1
                
            elif people[l] + people[r] > limit:
                r -= 1
                boat += 1

            elif people[l] + people[r] <= limit:
                l += 1
                r -= 1
                boat +=1 
        
        return boat

