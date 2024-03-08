class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Early return if the strings are of different lengths
        if len(s) != len(t):
            return False
        
        # Dictionaries to store character mappings
        map_s_to_t = {}
        map_t_to_s = {}
        
        for char_s, char_t in zip(s, t):
            # If mapping exists, check for consistency
            if (char_s in map_s_to_t and map_s_to_t[char_s] != char_t) or \
               (char_t in map_t_to_s and map_t_to_s[char_t] != char_s):
                return False
            
            # Create or update the mappings
            map_s_to_t[char_s] = char_t
            map_t_to_s[char_t] = char_s
        
        return True

