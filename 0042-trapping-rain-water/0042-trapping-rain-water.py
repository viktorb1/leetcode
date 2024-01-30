class Solution:
    def trap(self, height: List[int]) -> int:
        count = 0
        
        l, r = 0, len(height) - 1
        ml, mr = height[0], height[-1]
        
        while l < r:
            if ml <= mr:
                l += 1
                count += max(ml - height[l], 0)
                ml = max(height[l], ml)
            else:
                r -= 1
                count += max(mr - height[r], 0)
                mr = max(height[r], mr)
        
        
        return count