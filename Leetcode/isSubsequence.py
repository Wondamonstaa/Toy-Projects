class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        si, ti = 0, 0  # Pointers for s and t

        while si < len(s) and ti < len(t):
            if s[si] == t[ti]:
                si += 1  # Move to the next character in s
            ti += 1  # Always move to the next character in t

        return si == len(s)  # If si == len(s), s is a subsequence of t


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i = j = 0
        ss, tt = len(s), len(t)

        if not s and t:
            return True
        
        if s and not t:
            return False
        
        if not s and not t:
            return True

        while i < ss and j < tt:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
            
            if i == ss:
                return True
        
        return False


# New
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        s_ptr = 0

        for char in t:
            if s_ptr < len(s) and s[s_ptr] == char:
                s_ptr += 1

        return s_ptr == len(s)
