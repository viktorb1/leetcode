class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        most = max(candies)
        sol = []
        
        for c in candies:
            sol.append(c + extraCandies >= most)
            
        return sol