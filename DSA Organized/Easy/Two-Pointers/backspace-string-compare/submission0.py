# reverse two-pointer solution

# Time:  O(n + m)
# Space: O(n + m)

def backspaceCompare(s: str, t: str) -> bool:
    
    mstring = ""
    mstring2 = ""
    skip = 0
    skip2 = 0

    # pointers are starting at the end of the iterables
    left = len(s) - 1
    right = len(t) - 1

    # the order of the conditions matter! after condition is met, while loop restarts but decremented of course to prevent inf loop

    # this is for the first string parameter
    while left >= 0:
        if s[left] == "#":
            skip += 1
            left -= 1

        elif skip > 0:
            left -= 1
            skip -= 1
        else:
            mstring += s[left]
            left -= 1

    # this is for the second string parameter
    while right >= 0:
            if t[right] == "#":
                skip2 += 1
                right -= 1
    
            elif skip2 > 0:
                right -= 1
                skip2 -= 1
            else:
                mstring2 += t[right]
                right -= 1


    return mstring == mstring2

s = "a##c"

t = "#a#c"

print(backspaceCompare(s, t))