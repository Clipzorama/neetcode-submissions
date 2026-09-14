class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Anoter way of doing this solution with two pointers even though theres easier ways of doing it
        pause = "".join(s.split(" "))
        left = 0
        right = len(pause) - 1


        while left <= right:

            if not pause[left].isalnum():
                left += 1
                continue

            if not pause[right].isalnum():
                right -= 1
                continue

            if pause[left].lower() == pause[right].lower():
                left += 1
                right -= 1
            else:
                return False
        
        return True
        