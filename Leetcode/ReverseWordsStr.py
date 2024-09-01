class Solution:
    def reverseWords(self, s: str) -> str:
        
        #O1
        if not s:
            return ""

        #NOTE: this will store the result words for a string. O1
        r = list()

        #NOTE: this will split a string into separate words. O(N)
        l = s.split()
        
        #NOTE: or m = l.deepcopy() => creates a deep copy (Copies not only references like l.copy() but the entire objects into the memory of a new copy using memo)

        '''
        A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.

        A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.
        '''
        m = l.copy()

        #O(N)
        for i in range(len(l)):
            #O(1)
            r.append(m.pop())

        print(r)

        ''' 
        Total Time Complexity: O(N)+O(N)+O(N)+O(N)=O(N)O(N)+O(N)+O(N)+O(N)=O(N)
        Total Space Complexity: O(N)+O(N)+O(N)+O(N)=O(N)O(N)+O(N)+O(N)+O(N)=O(N)
        '''

        #O(N)
        return " ".join(r)
