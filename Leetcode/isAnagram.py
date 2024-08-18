from collections import Counter

class Solution:

    def isAnagram(self, s, t) -> bool:

        if len(s) != len(t):
            return False
        
        return Counter(s) != Counter(t)
   
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}

        for string in strs:
            sorted_string = "".join(sorted(string))

            if sorted_string in anagrams:
                anagrams[sorted_string].append(string)
            else:
                anagrams[sorted_string] = [string]

        result = list(anagrams.values())

        return result
