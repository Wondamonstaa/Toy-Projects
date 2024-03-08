class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:

        count: int = 0

        for i in words:
            if pref in i[0:len(pref)]:
                count+=1

        return count
