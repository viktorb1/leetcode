class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        num = 0
        
        for i in range(len(strs[0])):            
            for j in range(1, len(strs)):
                if strs[j-1][i] > strs[j][i]:
                    num += 1
                    break
                
        return num