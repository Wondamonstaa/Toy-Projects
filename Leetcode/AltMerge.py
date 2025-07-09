class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        merged = []

        l1, l2 = len(word1), len(word2)

        for i in range(max(l1, l2)):
            if i < l1:
                merged.append(word1[i])
            if i < l2:
                merged.append(word2[i])

        return ''.join(merged)


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        if not word1:
            return word2

        if not word2:
            return word1

        r = []
        l1, l2 = len(word1), len(word2)
    
        tail = word1[l2:] if l1 > l2 and l1 != l2 else word2[l1:]
        t = [w for w in tail]
        w1, w2 = [w for w in word1], [w for w in word2]
        
        if l1 >= l2:
            for i in range(l2):
                r.append(w1[i])
                r.append(w2[i])
        else:
            for i in range(l1):
                r.append(w1[i])
                r.append(w2[i])

        
        return "".join(r+t)
