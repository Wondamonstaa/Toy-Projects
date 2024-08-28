class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        words: List[str] = list()
        
        if not word1:
            return word2
        
        if not word2:
            return word1
        
        i = 0
        
        while (i < len(word1) or i < len(word2)):
            
            if i < len(word1):
                words.append(word1[i])
                
            if i < len(word2):
                words.append(word2[i])
            
            i += 1
        
        
        return "".join(words)
