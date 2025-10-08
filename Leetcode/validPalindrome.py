import re 

class Solution:
    def isPalindrome(self, s: str) -> bool:

        if not s:
            return False

        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        return s[::] == s[::-1]
        
