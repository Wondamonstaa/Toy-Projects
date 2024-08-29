class Solution:
    def reverseWords(self, s: str) -> str:
        
        l1 = s.split()
        l2 = list()
        
        for i in l1:
            l2.append(i)
        
        l2.reverse()
        
        r = ""
        for i in l2:
            r += i
            r += ' '
            
        final = r[:-1]
        
        return final
