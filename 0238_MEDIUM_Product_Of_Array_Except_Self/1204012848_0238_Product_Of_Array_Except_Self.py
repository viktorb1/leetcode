class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol = []
        prod = 1
        for n in nums:
            sol.append(prod)
            prod *= n
        
        prod = 1
        for i, n in enumerate(nums[::-1]):
            sol[len(nums)-1-i] *= prod
            prod *= n
        
        return sol
