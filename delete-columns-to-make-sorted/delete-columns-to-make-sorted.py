class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        num = 0
        
        for i in range(len(strs[0])):
            curr = strs[0][i]
            
            for j in range(len(strs)):
                if curr > strs[j][i]:
                    num += 1
                    break
                else:
                    curr = strs[j][i]
                    
                
                
        return num