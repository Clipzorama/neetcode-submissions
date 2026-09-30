# theres also this solution that is also as optimal as it can possibly be.

# time: O(n)
# space: O(n)

def reverseWords(self, s: str) -> str:
    # Removing all left and right space. extracting each word as one specific element and then reversing the list
    new_s = s.strip().split()[::-1]

    # convert back to a string and then we return
    return " ".join(new_s)