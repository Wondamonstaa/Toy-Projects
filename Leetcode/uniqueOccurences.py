from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        c = Counter(arr)
        e = set()

        for v in c.values():
            if v not in e:
                e.add(v)
            else:
                return False

        return True

# Option 2, if you want
def uniqueOccurrences(self, arr: List[int]) -> bool:
    counts = Counter(arr).values()
    return len(counts) == len(set(counts))
