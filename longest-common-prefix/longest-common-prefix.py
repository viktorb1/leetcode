class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        lcp = 0
        shortest = len(strs[0])
        
        for i in strs:
            if len(i) < shortest:
                shortest = len(i)
                
        for j in range(shortest):
            for k in range(len(strs)):
                if strs[k][j] != strs[0][j]:
                    return strs[0][:lcp];
            
            lcp += 1
            
            
        return strs[0][:shortest]
            