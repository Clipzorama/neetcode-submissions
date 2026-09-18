# reverse two-pointer solution --> MORE OPTIMAL SOLUTION

# Time:  O(n + m)
# Space: O(1)

def backspaceCompare(s: str, t: str) -> bool:
    left = len(s) - 1
    right = len(t) - 1


    # we want to make sure that both values are being counted for instead of exhausted
    while left >= 0 or right >= 0:


        # each iteration we make sure that there is no hashtags inside of each of these elements
        skip_s = 0
        while left >= 0:
            if s[left] == "#":
                skip_s += 1
                left -= 1

            elif skip_s > 0:
                left -= 1
                skip_s -= 1
            else:
                break

        # each iteration we make sure that there is no hashtags inside of each of these elements (same with t as well)
        
        skip_t = 0
        while right >= 0:
            if t[right] == "#":
                skip_t += 1
                right -= 1
            elif skip_t > 0:
                right -= 1
                skip_t -= 1
            else:
                break


        # outside of the while loop, we're checking if the letters are valid, if not then we return False
        if left >= 0 and right >= 0:
            if s[left] != t[right]:
                return False

        # if the first condition fails, then either left or right is at 0 which means they wouldnt be equal and this would be false again
        elif left >= 0 or right >= 0:
            return False

        # if everything is fine, we decrement and proceed with the algorithm 
        left -= 1
        right -= 1


    # return true if everything works out

    return True