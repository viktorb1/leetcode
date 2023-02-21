class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol = []
        
        prod = 1
        for num in nums:
            sol.append(prod)
            prod *= num
        
        prod = 1
        for i, num in enumerate(nums[::-1]):
            sol[len(nums)-i-1] *= prod
            prod *= num
        
        return sol