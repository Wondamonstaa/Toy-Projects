from typing import List

class Solution:
    def reverseWords(self, s: str) -> str:

        if not s:
            return ""

        words: List[str] = [char.strip() for char in s.split()]
        length: int = len(words)
        result: str = ""

        for i in range(length):
            
            temp = words.pop()
            result += temp + " "

        
        return result.rstrip()


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s = list(s)
        s = reversed(s)
        
        return ' '.join(s)
        
