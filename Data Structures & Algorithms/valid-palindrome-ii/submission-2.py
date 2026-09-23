# had to review this problem again but solved it

# time: O(n)
# space: O(1)

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                skip_left = s[left + 1: right + 1]
                skip_right = s[left:right]

                return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]
        

        return True