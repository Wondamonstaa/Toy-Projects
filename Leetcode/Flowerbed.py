class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        for i in range(len(flowerbed) - 1):
            
            left = i == 0 or flowerbed[i-1] == 0
            right = len(flowerbed) - 1 == 0 or flowerbed[i+1] == 0

            if left and right and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1
        
        return n <= 0
