class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        flowerbed = [0] + flowerbed + [0]
        for i in range(len(flowerbed)-2):
            if flowerbed[i] == flowerbed[i+1] == flowerbed[i+2] == 0:
                flowerbed[i+1] = 1
                count += 1
        
        return count >= n