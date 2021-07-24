class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        curr = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[curr] = nums[i]
                curr += 1       

        return curr
    
# ALTERNATIVE SOLUTION:
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#             j = len(nums) - 1
#             i = 0
            
#             while i <= j:
#                 if nums[i] == val:
#                     nums[i], nums[j] = nums[j], nums[i]
#                     j -= 1
#                 else:
#                     i += 1
                
#             return j+1;
