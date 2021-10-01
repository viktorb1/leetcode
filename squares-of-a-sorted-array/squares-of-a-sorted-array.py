class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sol = []
        
        for i in nums:
            sol.append(i ** 2)
        
        sol.sort()
        return sol