'''class Solution:
    def countBinarySubstrings(self, s: str) -> int:

        counter: int = 0

        if '0' in s and '1' not in s:
            return 1

        if '1' in s and '0' not in s:
            return 1

        if len(s) % 2 == 0:
            t: str = s[:len(s)//2]
            for i in range(0, len(t)-1):
                if t in s:
                    counter += 1
                t = s[:len(s)//2]
        else:
            half_index = (len(s) - 1) // 2
            t = s[:half_index]
            for i in range(0, len(t)-1):
                if t in s:
                    counter += 1
                t = s[:(len(s) + 1)//2]

        return counter*2'''

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        last = s[0]
        curcount = 1
        prevcount = 0

        ret = 0
        for i in s[1:]:
            if i == last:
                curcount += 1
            else:
                ret += min(curcount, prevcount)
                prevcount = curcount
                curcount = 1
                last = i

        ret += min(curcount, prevcount)

        return ret
        
