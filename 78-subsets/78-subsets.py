class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        n = len(nums)
        
        for m in range(2**n, 2**(n+1)):
            bitmask = bin(m)[3:]
            output.append([num for i, num in enumerate(nums) if bitmask[i] == '1'])
            
        return output