class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        saw = {};
        
        for i in range(len(nums)):
            if nums[i] not in saw:
                saw[nums[i]] = i
            elif saw[nums[i]] != i:
                return [saw[nums[i]], i]
            
            if target - nums[i] in saw and target - nums[i] != nums[i]:
                return [i, saw[target - nums[i]] ]

        
        return [];
            