class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
    
        def dfs(prev1, prev2, rem):
            if not rem:
                return True
            
            for i in range(1, len(rem)+1):
                if rem[0] == '0' and num[:i] != '0':
                    continue
                    
                if prev1 + prev2 == int(rem[:i]):
                    if dfs(prev2, int(rem[:i]), rem[i:]):
                        return True
            
            return False
        
        for i in range(2, len(num)+1):
            for j in range(1, i):
                if num[j] == '0' and num[j:i] != '0':
                    continue
                if num[0] == '0' and num[:j] != '0':
                    continue
                
                if num[i:] and dfs(int(num[:j]), int(num[j:i]), num[i:]):
                    return True
        
        return False
                