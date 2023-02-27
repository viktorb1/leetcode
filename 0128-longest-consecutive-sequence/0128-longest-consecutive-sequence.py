class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        avail = set(nums)
        count = 0
        
        for n in avail:
            if n-1 not in avail:
                cur = n
                total = 1
                while cur+1 in avail:
                    total += 1
                    cur += 1
                count = max(total, count)
        
        return count
                
