class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverser = ""
        for char in s:
            if char.isalnum():
                reverser += char.lower()
        
        
        return reverser == reverser[::-1]