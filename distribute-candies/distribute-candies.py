class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        numCandies = len(candyType)
        numCandyTypes = len(set(candyType))
        return min(numCandies//2, numCandyTypes)