class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        
        for i in nums:
            if not i in count:
                count[i] = 1
            else:
                count[i] += 1
        
        for val in count:
            if count[val] > len(nums) // 2:
                return val