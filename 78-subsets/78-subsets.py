class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
            
        def backtrack(nums, curr):
            if len(curr) == k:
                output.append(curr[:])
                return 
            
            for idx, num in enumerate(nums):
                curr.append(num)
                backtrack(nums[idx+1:], curr)
                curr.pop()
        
        output = []

        for k in range(len(nums) + 1):
            backtrack(nums, [])
        
        return output
                
            
        