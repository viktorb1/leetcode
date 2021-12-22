class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        saw = dict()
        
        for idx, num in enumerate(nums):
            if target-num in saw:
                return [saw[target-num], idx]
            
            saw[num] = idx
