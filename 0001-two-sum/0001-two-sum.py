class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        
        for i, n in enumerate(nums):
            if target - n in seen:
                return [seen[target - n], i]
            
            seen[n] = i