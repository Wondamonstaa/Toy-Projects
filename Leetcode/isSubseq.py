class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        assert all(v is not None for v in [s,t])

        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1

            # this guy must always move forward
            j += 1

        # the end of 's' has been reached
        return len(s) == i
        
