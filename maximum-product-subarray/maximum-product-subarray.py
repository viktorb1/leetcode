class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max = float('-inf')
        local_max = 1
        local_min = 1
        
        for num in nums:
            vals = (num, num*local_max, num*local_min)
            local_max = max(vals)
            local_min = min(vals)
            global_max = max(global_max, local_max)
            
        return global_max