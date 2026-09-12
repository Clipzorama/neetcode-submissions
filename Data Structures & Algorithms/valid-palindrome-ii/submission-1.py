class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

            # think:

            # “What if I skip left?”

            # “What if I skip right?”

        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1

            # instead of putting chances --> variable flag, we just check right away
            else:
                # skipping left logic if palindrome after. (remeber :stop is exclusive so we want to count the current right element with + 1)
                skip_left = s[left + 1 : right + 1] 

                # skipping right logic (already exclusive so (left:right))
                skip_right = s[left:right]

                return skip_left[:] == skip_left[::-1] or skip_right[:] == skip_right[::-1]

        return True