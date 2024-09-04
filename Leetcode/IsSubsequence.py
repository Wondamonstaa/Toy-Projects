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
