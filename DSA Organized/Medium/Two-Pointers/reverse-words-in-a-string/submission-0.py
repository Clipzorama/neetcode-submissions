
# this is the most optimal solution but here were using a deque

# time: O(n)
# space: O(n)

class Solution:
    def reverseWords(self, s: str) -> str:
        # initialize the deque
        result = deque()

        # making our flags here
        start = 0
        i = 0

        while i < len(s):

            # then we know where the first word is present
            if s[i] != " ":
                start = i

                # get everything inside of the word until i reaches a space
                while i < len(s) and s[i] != " ":
                    i += 1

                # we append the sliced result to the left
                result.appendleft(s[start:i])

            # then we increment to the next word
            i += 1

        # we turn everything into a string once done
        return " ".join(result)