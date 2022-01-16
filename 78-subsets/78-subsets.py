class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        
        for num in nums:
            nex = []
            
            for ele in output:
                nex.append(ele + [num])
            
            output += nex
        
        return output
            