class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        twonums = nums + nums
        stack = []
        next_greater = [-1 ] * len(twonums)
        
        for i, n in enumerate(twonums):
            while stack and twonums[stack[-1]] < n:
                next_greater[stack.pop()] = n
            stack.append(i)
        
        return next_greater[:len(nums)]