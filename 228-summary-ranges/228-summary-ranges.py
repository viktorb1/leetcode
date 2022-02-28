class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        sol = []
        i = 0
        
        while i < len(nums):
            start, end = i, i

            while i < len(nums) - 1 and nums[i] + 1 == nums[i+1]:
                end += 1
                i += 1
            
            if start == end:
                sol.append(str(nums[start]))
            else:
                sol.append(str(nums[start]) + '->' + str(nums[end]))
            
            i += 1
        
        return sol
                