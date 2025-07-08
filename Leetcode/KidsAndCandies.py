class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        if not candies:
            return [False] * len(candies)

        m = max(candies)
        c1 = candies.copy()

        for c in range(len(c1)):
            c1[c] += extraCandies

        c1 = [True if w >= m else False for w in c1]
        #c1 = [w > m for w in c1]
    
        return c1
