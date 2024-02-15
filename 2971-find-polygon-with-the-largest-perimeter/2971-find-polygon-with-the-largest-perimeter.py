class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort() # sort nums
        prev_sum = 0
        max_sum = -1
        
        for n in nums: # let n be the longest edge
            if prev_sum > n: # compare it to sum of all previous smaller edges
                max_sum = max(max_sum, prev_sum + n)
            
            prev_sum += n
        
        return max_sum