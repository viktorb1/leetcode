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
            
# Alternative solution using Boyer-Moore Voting Algorithm
# 
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         curr = nums[0]
#         count = 0
        
#         for i in nums:
#             if curr != i and count > 1:
#                 count -= 1
#             elif curr != i:
#                 curr = i
#                 count = 1
#             else:
#                 count += 1
            
#         return curr
