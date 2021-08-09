class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        
        start = nums[0]
        ranges = []
        
        for i in range(len(nums)):
            if i == len(nums) - 1 or nums[i] + 1 < nums[i+1]: # last element or next element is greater by more than one
                if start == nums[i]:
                    ranges.append(str(start))
                else:
                    ranges.append(str(start) + '->' + str(nums[i]))
                    
                if len(nums) > i+1: # set next start element
                    start = nums[i+1]
            
        return ranges
