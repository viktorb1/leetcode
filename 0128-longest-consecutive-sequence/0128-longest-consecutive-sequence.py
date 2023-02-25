class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        avail = set(nums)
        max_cons = 0
        
        for n in avail:
            count = 1
            if n-1 not in avail:
                while n + 1 in avail:
                    count += 1
                    n += 1

                max_cons = max(max_cons, count)

        return max_cons
    

