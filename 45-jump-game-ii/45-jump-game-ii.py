from collections import deque
class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        count = 0
        
        while r < len(nums) - 1:
            new_r = float('-inf')
            
            for i in range(l, r+1):
                new_r = max(new_r, i + nums[i])
            
            l, r = r, new_r
            count += 1
        
        return count