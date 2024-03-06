class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        si, ti = 0, 0  # Pointers for s and t

        while si < len(s) and ti < len(t):
            if s[si] == t[ti]:
                si += 1  # Move to the next character in s
            ti += 1  # Always move to the next character in t

        return si == len(s)  # If si == len(s), s is a subsequence of t
