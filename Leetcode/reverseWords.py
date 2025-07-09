class Solution:
    def reverseWords(self, s: str) -> str:

        """
        2 pointers
        """

        i, j = 0, len(s) -1
        s = s.strip().split()
        s1 = []
        
        for i in s:
            s1.append(i)
            s1.append(" ")
        
        r = "".join(reversed(s1))
        r = r.lstrip(" ")

        return r
