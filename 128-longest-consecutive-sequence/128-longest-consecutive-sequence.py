class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        options = set(nums)
        max_count = 0
        
        for n in nums:
            if n-1 not in options:
                count = 1
                x = n
                while x+1 in options:
                    count += 1
                    x += 1
                    
                max_count = max(max_count, count)
            
        return max_count