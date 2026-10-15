# TIME COMPLEXITY: O(log n)
# - We iterate through each digit of the number to calculate the sum of its squares.
# - An integer n has approximately log₁₀(n) digits.
# - The numbers quickly become smaller, and the Hash Set prevents infinite cycles.
# - Therefore, the overall time complexity is O(log n).

# SPACE COMPLEXITY: O(log n)
# - We use a Hash Set (seen) to store previously encountered numbers.
# - We also convert integers into strings using str(total), which requires space proportional to the number of digits.
# - Therefore, the overall space complexity is O(log n).


class Solution:
    def isHappy(self, n: int) -> bool:

        total = n
        seen = set()

        while total != 1:
            # if total is in the set, there'll be a never ending cycle
            if total in seen:
                return False
            
            # we add it in and then calculate the next number
            seen.add(total)

            res = 0

            # convert to a string and do the calculation
            for digit in str(total):
                res += int(digit) ** 2
            
            total = res
        
        return True


        