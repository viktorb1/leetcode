from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol = []
        
        for i in permutations(nums):
            sol.append(i)
        
        return sol